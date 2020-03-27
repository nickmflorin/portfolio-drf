import pytest


@pytest.mark.django_db
def test_skill_added_to_education_project(create_education, create_project, create_skill):
    """
    If a given skill is added to a project, the skill should also be added to
    the education or experience governing that project.

    NOTE:
    ----
    We need to investigate whether or not the extra saving is necessary,
    because the forms might handle the save of the related model themselves.
    """
    education = create_education()
    projects = [
        create_project(content_object=education),
        create_project(content_object=education)
    ]
    skill1 = create_skill(name="Python")
    skill1.educations.add(education)
    assert [skill.pk for skill in education.skills.all()] == [skill1.pk]

    skill2 = create_skill(name="Java")
    projects[0].skills.add(skill2)
    assert [skill.pk for skill in education.skills.all()] == [skill1.pk, skill2.pk]


@pytest.mark.django_db
def test_skill_added_to_education_course(create_education, create_course, create_skill):
    """
    If a given skill is added to a project, the skill should also be added to
    the education or experience governing that project.

    NOTE:
    ----
    We need to investigate whether or not the extra saving is necessary,
    because the forms might handle the save of the related model themselves.
    """
    education = create_education()
    courses = [
        create_course(education=education),
        create_course(education=education)
    ]
    skill1 = create_skill(name="Python")
    skill1.educations.add(education)
    assert [skill.pk for skill in education.skills.all()] == [skill1.pk]

    skill2 = create_skill(name="Java")
    courses[0].skills.add(skill2)
    assert [skill.pk for skill in education.skills.all()] == [skill1.pk, skill2.pk]
