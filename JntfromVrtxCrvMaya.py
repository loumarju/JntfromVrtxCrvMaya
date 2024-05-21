#Create a joint in the position of a vertex

import maya.cmds as cmds

#Convert selection to vertices

vertices = cmds.ls(selection=True)

for i, vert in enumerate(vertices):
    #Get the position of the vertices
    position = cmds.pointPosition(vert)

    # Create a joint at the position of the vertex
    cmds.joint(name='NewJoint{}'.format(i), position=position)
