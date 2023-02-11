from projectWildFarm.customer import Customer
from projectWildFarm.equipment import Equipment
from projectWildFarm.exercise_plan import ExercisePlan
from projectWildFarm.gym import Gym
from projectWildFarm.subscription import Subscription
from projectWildFarm.trainer import Trainer

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))

