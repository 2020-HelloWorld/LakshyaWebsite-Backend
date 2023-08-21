from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from common.models import company
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from internships.models import *
import json



# def internship_list_view(request):
#     internships = Internship.objects.all()
#     serializer = InternshipSerializer(internships, many=True)
#     return JsonResponse(serializer.data, safe=False)

# def internship_detail_view(request):
#     internship_id = request.data.get('internship_id')
#     internship = get_object_or_404(Internship, internship_id=internship_id)
#     serializer = InternshipSerializer(internship)
#     return JsonResponse(serializer.data)

# @login_required
# def add_internship_view(request):
#     serializer = InternshipSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return JsonResponse(serializer.data, status=201)
#     return JsonResponse(serializer.errors, status=400)


def internship_list_view(request):
    interships = Internship.objects.all()
    intern_data = []
    for intern_obj in interships:
        intern_data.append({
            'internship_id': intern_obj.internship_id,
            'apply_before': intern_obj.apply_before,
            'company': intern_obj.company.name,
            'title':intern_obj.title,
            'start_date': intern_obj.startdate,
            'type': intern_obj.type,
            'stipend' : intern_obj.stipend,
            'isHiring': intern_obj.isHiring,
            'isRemote': intern_obj.isRemote,

        

        })
    return JsonResponse(intern_data, safe=False)

def internship_detail_view(request, internship_id):
    intern_obj = get_object_or_404(Internship, internship_id=internship_id)
    intern_data = {
        'internship_id': intern_obj.internship_id,
        'description': intern_obj.description,
        'company': intern_obj.company.name,
        'startDate': intern_obj.startDate,
        'duration': intern_obj.duration,
        'stipend': intern_obj.stipend,
        'aboutCompany': intern_obj.aboutCompany,
        'whoCanApply': intern_obj.whoCanApply,
        'perks': intern_obj.perks,
        'numberofopenings': intern_obj.numberofopenings,
    }
    return JsonResponse(intern_data)


# def add_internship_view(request):
#     if request.method == 'POST':
#         data = request.POST
#         skill_name = data.get('skill_name')
#         try:
#             skill_obj = tag.get(name = skill_name)

#         except:
#             skill_obj = tag(name = skill_name)
#             skill_obj.save()

#         internship_obj = internship(skill_id = skill_obj.id)
#         internship_obj.save()
#         return JsonResponse({'message': 'Internship added successfully'}, status=201)
    
#     return JsonResponse({'error': 'Invalid request method'}, status=400)

# def internship_add_new(req):
#     data = req.POST
#     skill_name = data.get('skill_name')
#     skill_obj = skills.objects.create(name = skill_name)




def add_internship_view(req):
    if not req.user.is_authenticated:
        response =  JsonResponse({'message': 'REDIRECT'}, status=302)
        return response
    if req.method == 'POST':
        data = json.loads(req.body.decode('utf-8'))
        print(data)
        newInternship = Internship(
            title = data['internshipTitle'],
            location = data['location'],
            description = data['description'],
            stipend =data['stipend'],
            type = data['type'],
            company = company.objects.get(email=req.user),
            skills = ", ".join(list(map(lambda x:x['content'],data['skills']))),
            startDate = data['startdate'],
            whoCanApply = ", ".join(list(map(lambda x:x['content'],data['whocanApply']))),
            openings = data['numberOfOpenings'],
            perks = data['perks'],
            apply_before = data['apply_before'],
            duration = data['duration'],
            aboutCompany = data['aboutCompany'],
            postedTime = data['postedTime'],
            numberofhiring = data['numberofhiring'],
            numberofopportunities = data['numberofopportunities'],
        
        )
    newInternship.save()
    return JsonResponse({"message":"SUCCESS"},status=201)






def apply_internship_view(req):
    if not req.user.is_authenticated:
        response =  JsonResponse({'message': 'REDIRECT'}, status=302)
        return response
    internshipId = json.loads(req.body.decode('utf-8'))['jobId']
    newApplication = internshipApplied(
        job = Internship.objects.get(id=internshipId),
        candidate = candidate.objects.get(email=req.user)
    )
    newApplication.save()
    return JsonResponse({"message":"SUCCESS"},status=201)