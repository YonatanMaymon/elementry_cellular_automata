from model import Model
from front import Front
import time

model = Model(110)
front = Front(model)


while front.is_open:
    model.step()
    front.step()