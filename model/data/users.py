import dataclasses


@dataclasses.dataclass
class User:
    full_name: str
    email: str
    addr: str
    permanent_addr: str


student = User(full_name='Vasya Pupkin', email='vsya@gmail.com', addr='sovet union', permanent_addr='ne dom i ne ulitsa')
