import logging
import copy
import json
bi_logger = logging.getLogger("bi")


def bilogger(user, view, **kwargs):
    data = copy.copy(kwargs)

    if "type" not in kwargs:
        data["type"] = "ok"

    data['user'] = 'anon'
    if not user.is_anonymous():
        data['user'] = user.id
    data['view'] = view.get_view_name()

    if "action" not in kwargs:
        data['action'] = view.action

    bi_logger.info(json.dumps(data))
