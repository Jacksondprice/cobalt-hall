from faker import Faker

fake = Faker()


def demo_students(count: int = 50) -> list[dict]:
    return [
        {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "date_of_birth": fake.date_of_birth(minimum_age=11, maximum_age=18).isoformat(),
            "guardian_email": fake.email(),
            "guardian_phone": fake.phone_number(),
        }
        for _ in range(count)
    ]
