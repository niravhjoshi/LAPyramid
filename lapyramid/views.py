from pyramid.view import view_config

import lapyramid.utils


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return extend_model({'project': 'Nirav index file'})



def extend_model(model_dict):
    model_dict['build_cache_id'] = lapyramid.utils.build_cache_id
    return model_dict