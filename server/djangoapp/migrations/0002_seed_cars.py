from django.db import migrations


def seed_cars(apps, schema_editor):
    CarMake = apps.get_model("djangoapp", "CarMake")
    CarModel = apps.get_model("djangoapp", "CarModel")

    cars = [
        ("Toyota", "Reliable Japanese automobile manufacturer", "Camry", "SEDAN", 2024, "Blue"),
        ("Ford", "American automobile manufacturer", "Explorer", "SUV", 2023, "Black"),
        ("Honda", "Japanese automobile and motorcycle manufacturer", "CR-V", "SUV", 2024, "White"),
    ]

    for make_name, description, model_name, car_type, year, color in cars:
        make, _ = CarMake.objects.get_or_create(
            name=make_name,
            defaults={"description": description},
        )
        CarModel.objects.get_or_create(
            car_make=make,
            name=model_name,
            defaults={"type": car_type, "year": year, "color": color},
        )


def remove_seed_cars(apps, schema_editor):
    CarMake = apps.get_model("djangoapp", "CarMake")
    CarMake.objects.filter(name__in=["Toyota", "Ford", "Honda"]).delete()


class Migration(migrations.Migration):
    dependencies = [("djangoapp", "0001_initial")]

    operations = [migrations.RunPython(seed_cars, remove_seed_cars)]
