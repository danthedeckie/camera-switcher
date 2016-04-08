Camera Switcher
===============

In order to switch active cameras in a blender scene, you need to:

1. Select that camera
2. ``View Menu > Cameras > Set Active Object as Camera (Ctrl-Num 0)``

To insert a 'cut' point in the timeline to cut to that camera in recording:

1. Select the camera
2. Insert a marker on the timeline ``(m)``
3. ``(Timeline) View Menu > Bind Cameras to Marker (Ctrl-B)``

The marker will be named by its frame number, F_42, for instance.

This is obviously extremely clumsy for scenes which switch cameras a lot. This addon introduces a much easier workflow.  It also allows switching between custom views of an object much easier.

How to install it:
------------------

1. Download the latest version of the python script from:

   https://bitbucket.org/dfairhead/camera-switcher/src/

2. Open Blender.

3. ``File > User Preferences > Add-ons > Install from File...``

4. Select the downloaded script.

5. Activate it.

How to use this addon:
----------------------

In the 3D view, open the Tool Shelf. ``(t)``  A new panel 'Camera Switcher'
should be there.  It lists all the available cameras, with ``Preview``
(to view the scene from that camera) and ``Take`` to insert a marker in
the timeline which cuts to that camera (and is named after that camera).

The ``Take`` buttons can be used while the scene is actually playing,
to 'live switch' through a scene.

