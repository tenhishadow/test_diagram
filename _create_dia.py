# diagram.py


try:
    from diagrams import Diagram
    found = True
except ImportError:
    found = False

from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram(name="image", outformat="png", show=False):
    ELB("lb") >> EC2("web") >> RDS("userdb")
