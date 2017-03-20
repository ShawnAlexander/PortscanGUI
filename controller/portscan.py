import asyncio
import socket
import multiprocessing


# Input data to this class are IP address objects piped from ping


class PortScanner(multiprocessing.Process):

    COMMON_PORTS = (21,     #FTP
                    22,     #SSH
                    23,     # Telnet
                    25,     # SMTP
                    49,     # TACACS
                    53,     # DNS
                    67,     # DHCP (UDP)
                    68,     # DHCP (UDP)
                    69,     # TFTP (UDP)
                    80,     # HTTP
                    88,     # Kerberos
                    110,    # POP3
                    111,    # RPC
                    123,    # NTP (UDP)
                    135,    # Windows RPC
                    137,    # NetBIOS
                    138,    # NetBIOS
                    139,    # SMB
                    143,    # IMAP
                    161,    # SNMP (UDP)
                    179,    # BGP
                    201,    # AppleTalk
                    389,    # LDAP
                    443,    # HTTPS
                    445,    # SMB
                    500,    # ISAKMP (UDP)
                    514,    # Syslog
                    520,    # RIP
                    546,    # DHCPv6
                    547,    # DHCPv6
                    587,    # SMTP
                    902,    # VMWare
                    1080,   # SOCKS
                    1194,   # VPN
                    1433,   # MS-SQL
                    1434,   # MS-SQL
                    1521,   # Oracle
                    1629,   # DameWare
                    2049,   # NFS
                    3128,   # Squid Proxy
                    3306,   # MySQL
                    3389,   # RDP
                    5060,   # SIP
                    5222,   # Jabber
                    5432,   # Postgres
                    5666,   # Nagios
                    5900,   # VNC
                    6000,   # X11
                    6129,   # DameWare
                    6667,   # IRC
                    9001,   # TOR/HSQL
                    9090,   # Openfire
                    9091,   # Openfire
                    9100    # Jet Direct

    )

    def __init__(self, queue, timeout = ):
        multiprocessing.Process.__init__(self)
        self.cancel = False
        self.timeout = timeout * 1000 # Convert to milliseconds
        self.inputQueue = queue

    def setTimeout(self, timeout):
        self.timeout = timeout

    async def KnockKnock(self, host, port):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
            client.setblocking(False)
            client.settimeout(self.timeout)
            await client.connect((host, port))
        except (OSError, BlockingIOError, ConnectionError, TimeoutError):
            client.close()
            # TODO: Add to unresponsive/error list
            return False
        client.close()
        return True

    async def PortScanDispatch(self, ip_object):
        for p in PortScanner.COMMON_PORTS:
            anybodyThere = await self.KnockKnock(ip_object.getIpStr(), p)
            if anybodyThere:
                ip_object.addPort(p)

    async def IPScanDispatch(self):
        while not self.cancel:
            ip_obj = await self.inputQueue.get()
            await self.PortScanDispatch(ip_obj)


    def run(self):
        ioloop = asyncio.get_event_loop()
        ioloop.run_until_complete(self.IPScanDispatch())
        ioloop.close()