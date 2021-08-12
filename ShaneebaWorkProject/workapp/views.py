
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework import status
class WorksGetPost(APIView):
    def get(self, request):
        res_data = list(Works.objects.all().values())
        return Response(res_data, status=status.HTTP_200_OK)

    def post(self, request):
        dict_data = request.data
        fk_project_id_id = dict_data["fk_project_id_id"] #1
        ins_project = Project.objects.get(id=fk_project_id_id)
        fk_type_id_id = dict_data["fk_type_id_id"]
        ins_worktype = WorkType.objects.get(id=fk_type_id_id)
        fk_work_status_id_id = dict_data["fk_work_status_id_id"]
        ins_work_status = WorkStatus.objects.get(id=fk_work_status_id_id)

        Works.objects.create(str_title=dict_data["str_title"], txt_descrption=dict_data["txt_descrption"],
                                         fk_project_id=ins_project,
                                         jsn_attachment=dict_data["jsn_attachment"],
                                         dbl_estimatation=dict_data["dbl_estimatation"],
                                         dat_start=dict_data["dat_start"],
                                         dat_end=dict_data["dat_end"], fk_type_id=ins_worktype,
                                         dat_approved=dict_data["dat_approved"], fk_work_status_id=ins_work_status,
                                         dbl_taken=dict_data["dbl_taken"],
                                         int_active=dict_data["int_active"])
        return Response('saved', status=status.HTTP_400_BAD_REQUEST)


class WorkUpdateDelete(APIView):
    def get(self, request, id):
        res_data = Works.objects.filter(id=id).values()
        print(res_data)
        return Response(res_data, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        dict_data = request.data
        fk_project_id_id = dict_data["fk_project_id_id"]
        ins_project = Project.objects.get(id=fk_project_id_id)
        fk_type_id_id = dict_data["fk_type_id_id"]
        ins_worktype = WorkType.objects.get(id=fk_type_id_id)
        fk_work_status_id_id = dict_data["fk_work_status_id_id"]
        ins_work_status = WorkStatus.objects.get(id=fk_work_status_id_id)
        ins_works = Works.objects.get(id=id)
        ins_works.str_title=dict_data["str_title"]
        ins_works.text_descrption=dict_data["txt_descrption"]
        ins_works.fk_project_id=ins_project
        ins_works.jsn_attachment = dict_data["jsn_attachment"]
        ins_works.dbl_estimatation = dict_data["dbl_estimatation"]
        ins_works.dat_start = dict_data["dat_start"]
        ins_works.dat_end = dict_data["dat_end"]
        ins_works.fk_type_id = ins_worktype
        ins_works.dat_approved = dict_data["dat_approved"]
        ins_works.fk_work_status_id = ins_work_status
        ins_works.dbl_taken = dict_data["dbl_taken"]
        ins_works.int_active = dict_data["int_active"]
        ins_works.save()
        return Response("updated", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        rst_data = Works.objects.get(id=id)
        rst_data.delete()
        return Response("deleted")
