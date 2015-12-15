import json
from resume.models import Resume, Project, ProfileEntry, ExpertiseEntry, WorkAchievement, WorkHistoryEntry, \
    ImportantLink


class Provisioner:
    @staticmethod
    def deserialize(obj_name):
        print 'Deserializing {}'.format(obj_name)
        return [d['fields'] for d in json.load(open('data/{}.json'.format(obj_name)))]

    @staticmethod
    def create_profile():
        resume = None
        for e in Provisioner.deserialize('Resume'):
            resume = Resume.objects.create(
                name=e['name'],
                phone=e['phone'],
                email=e['email'],
                url=e['url'],
            )

        for e in Provisioner.deserialize('Project'):
            print Project.objects.create(
                name=e['name'],
                short_description=e['short_description'],
                long_description=e['long_description'],
                deployment_url=e['deployment_url'],
                src_url=e['src_url'],
                sort_order=e['sort_order'],
                resume=resume,
            )
        for e in Provisioner.deserialize('ImportantLink'):
            print ImportantLink.objects.create(
                description=e['description'],
                url=e['url'],
                sort_order=e['sort_order'],
                resume=resume,
            )
        for e in Provisioner.deserialize('ProfileEntry'):
            print ProfileEntry.objects.create(
                entry=e['entry'],
                sort_order=e['sort_order'],
                resume=resume,
            )
        original_ids = {}
        for e in Provisioner.deserialize('ExpertiseEntry'):
            print ExpertiseEntry.objects.create(
                entry=e['entry'],
                entry_details=e['entry_details'],
                sort_order=e['sort_order'],
                resume=resume,
            )
        for e in Provisioner.deserialize('WorkHistoryEntry'):
            entry = WorkHistoryEntry.objects.create(
                client_name=e['client_name'],
                title=e['title'],
                contract=e['contract'],
                location=e['location'],
                timespan=e['timespan'],
                sort_order=e['sort_order'],
                resume=resume,
            )
            print entry
            original_ids[entry.pk] = entry
        for e in Provisioner.deserialize('WorkAchievement'):
            print WorkAchievement.objects.create(
                entry=original_ids[e['entry']],
                description=e['description'],
                sort_order=e['sort_order'],
            )
