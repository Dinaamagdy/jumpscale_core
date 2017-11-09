from js9 import j
import os
import capnp

ModelBaseCollection = j.data.capnp.getModelBaseClassCollection()
ModelBase = j.data.capnp.getModelBaseClass()
from JumpScale9.clients.tarantool.KVSInterface import KVSTarantool


class UserModel(ModelBase):
    '''
    '''
    pass


class UserCollection(ModelBaseCollection):
    '''
    This class represent a collection of Users
    It's used to list/find/create new Instance of User Model object
    '''

    def __init__(self):
        self.logger = j.logger.get('model.user')
        category = 'user'
        namespace = ""

        # instanciate the KVS interface on top of tarantool
        cl = j.clients.tarantool.client_get()  # will get the tarantool from the config file, the main connection
        db = KVSTarantool(cl, category)

        mpath = j.sal.fs.getDirName(os.path.abspath(__file__)) + "/model.capnp"
        SchemaCapnp = j.data.capnp.getSchemaFromPath(mpath, name='User')

        super().__init__(SchemaCapnp, category=category, namespace=namespace, modelBaseClass=UserModel, db=db, indexDb=db)

    def new(self):
        return UserModel(collection=self, new=True)

    def get(self, key):
        return UserModel(key=key, collection=self, new=False)

    # BELOW IS ALL EXAMPLE CODE WHICH NEEDS TO BE REPLACED

    def list(self):
        """
        list all key in this collection
        """
        return self._db.list()

    def find(self):
        raise NotImplementedError()

    def delete(self, key):
        self._db.delete(key=key)
