from django.db import migrations


def expand_car_catalog(apps, schema_editor):
    CarMake = apps.get_model("djangoapp", "CarMake")
    CarModel = apps.get_model("djangoapp", "CarModel")

    catalog = {
        "NISSAN": ["Pathfinder", "Qashqai", "XTRAIL"],
        "Mercedes": ["A-Class", "C-Class", "E-Class"],
        "Audi": ["A4", "A5", "A6"],
        "Kia": ["Sorrento", "Carnival", "Cerato"],
        "Toyota": ["Corolla", "Camry", "Kluger"],
    }

    for make_name, model_names in catalog.items():
        make, _ = CarMake.objects.get_or_create(
            name=make_name,
            defaults={"description": "Established automobile manufacturer"},
        )
        for model_name in model_names:
            CarModel.objects.get_or_create(
                car_make=make,
                name=model_name,
                defaults={"type": "SUV", "year": 2023, "color": "Black"},
            )


class Migration(migrations.Migration):
    dependencies = [("djangoapp", "0002_seed_cars")]

    operations = [migrations.RunPython(expand_car_catalog, migrations.RunPython.noop)]
