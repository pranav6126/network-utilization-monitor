from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel

def createNetwork():
    net = Mininet(controller=Controller)

    print("*** Creating nodes")
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')

    s1 = net.addSwitch('s1')

    print("*** Creating links")
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)

    print("*** Starting network")
    net.start()

    CLI(net)

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    createNetwork()
