# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class PackageConfig(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = PackageConfig()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPackageConfig(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # PackageConfig
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # PackageConfig
    def Packages(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Package import Package
            obj = Package()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # PackageConfig
    def PackagesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # PackageConfig
    def PackagesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def Start(builder): builder.StartObject(1)
def PackageConfigStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddPackages(builder, packages): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(packages), 0)
def PackageConfigAddPackages(builder, packages):
    """This method is deprecated. Please switch to AddPackages."""
    return AddPackages(builder, packages)
def StartPackagesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def PackageConfigStartPackagesVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartPackagesVector(builder, numElems)
def End(builder): return builder.EndObject()
def PackageConfigEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)