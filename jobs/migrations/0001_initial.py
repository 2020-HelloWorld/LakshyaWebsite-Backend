# Generated by Django 4.2.3 on 2023-07-19 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                ("job_id", models.AutoField(primary_key=True, serialize=False)),
                ("description", models.TextField()),
                ("apply_before", models.DateField()),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jobs.company"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="JobSkill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jobs.job"
                    ),
                ),
                (
                    "skill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jobs.skill"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="job",
            name="skills_required",
            field=models.ManyToManyField(through="jobs.JobSkill", to="jobs.skill"),
        ),
    ]