import logging
import copy
import json
bi_logger = logging.getLogger("bi")


def bilogger(request, view, obj=None, **kwargs):
    data = copy.copy(kwargs)

    data["ip"] = request.META.get("REMOTE_ADDR", None)
    data["user-agent"] = request.META.get("HTTP_USER_AGENT", None)
    data["path"] = request.get_full_path()

    if "type" not in kwargs:
        data["type"] = "ok"

    data['user'] = 'anon'
    if not request.user.is_anonymous():
        data['user'] = request.user.id
    data['view'] = view.get_view_name()

    if "action" not in kwargs:
        data['action'] = view.action

    if obj is not None:
        data['object-id'] = obj.id
        if hasattr(obj, 'project_id'):
            data['project-id'] = obj.project_id

    bi_logger.info(json.dumps(data))
