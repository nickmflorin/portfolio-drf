from portfolio.app.common.forms import HorizonForm
from .models import Experience


class ExperienceForm(HorizonForm):

    class Meta:
        model = Experience
        fields = '__all__'
