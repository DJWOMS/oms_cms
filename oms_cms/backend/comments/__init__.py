default_app_config = 'oms_cms.backend.comments.apps.CommentsConfig'


def get_model():
    from oms_cms.backend.comments.models import OmsComment
    return OmsComment
