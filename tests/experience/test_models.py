import pytest


@pytest.mark.django_db
def test_skill_added_to_experience_project(create_experience, create_project, create_skill):
    """
    If a given skill is added to a project, the skill should also be added to
    the education or experience governing that project.

    NOTE:
    ----
    We need to investigate whether or not the extra saving is necessary,
    because the forms might handle the save of the related model themselves.
    """
    experience = create_experience()
    projects = [
        create_project(content_object=experience),
        create_project(content_object=experience)
    ]
    skill1 = create_skill(name="Python")
    skill1.experiences.add(experience)
    assert [skill.pk for skill in experience.skills.all()] == [skill1.pk]

    skill2 = create_skill(name="Java")
    projects[0].skills.add(skill2)
    assert [skill.pk for skill in experience.skills.all()] == [skill1.pk, skill2.pk]
