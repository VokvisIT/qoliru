from django.core.management.base import BaseCommand
from dashboard.models import Region, Source, Resource, ModelDataTest
from .parser_vk import get_vk_wall_posts, get_group_id
from datetime import datetime, timedelta
import pytz
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Parse VK data for the last day'

    def handle(self, *args, **options):
        token = 'vk1.a.5uEA0WWcvx91FS4UhMFvjdRzjJCoV1JlijQphi0paAaocmJysNkFvhxGL40l7SSrUDHSBHo7waTME8bC38pYqrjURbgsW0Dn8MfVOJ98d753CZOfLgN_MpDFDEZ7GcLp1u_Ga9dQA2pv83N6h4pQY6q97Nt6JPx88ZmtzHTszQe_bNeX4Ecj4yYgTcYtd2GTKe9QPLj0bANiyWZFhsNI3w'
        version = '5.131'
        end_date = datetime.now(pytz.timezone('Europe/Moscow')) - timedelta(days=2)
        resources = Resource.objects.filter(source__name='ВКонтакте')
        for resource in resources:
            group_id = get_group_id(token, version, resource.link)
            if group_id is not None:
                get_vk_wall_posts(token, version, group_id, end_date, resource.name, resource)
