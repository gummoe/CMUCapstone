def index():
    redirect(URL('submit_addresses'))


def submit_addresses():
    session.test = "initialvalue"
    node_list = []
    form = FORM(
                TEXTAREA(_name='address', requires=IS_NOT_EMPTY()),
                INPUT(_type='submit'))
    if form.accepts(request, session):
        #Parse submission
        session.addresses = form.vars.address
        addresses = form.vars.address
        address_lines = addresses.splitlines()

        #Geocode each address and add to node_list
        for line in address_lines:
            temp = Node(line)
            temp.geocode()
            node_list.append(temp)

        matrix = NodeMatrix(node_list)
        matrix.get_matrix()
        print matrix.duration_matrix
        print matrix.distance_matrix
        session.duration_matrix = matrix.duration_matrix
        session.distance_matrix = matrix.distance_matrix

        #Comment the line below to see same-page form submission results
        redirect(URL('form_response'))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return dict(form=form)


def form_response():
    return dict(duration_matrix=session.duration_matrix, distance_matrix=session.distance_matrix)



def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())