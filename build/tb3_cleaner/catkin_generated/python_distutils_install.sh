#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/dody3333/catkin_ws/src/tb3_cleaner"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/dody3333/catkin_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/dody3333/catkin_ws/install/lib/python2.7/dist-packages:/home/dody3333/catkin_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/dody3333/catkin_ws/build" \
    "/usr/bin/python2" \
    "/home/dody3333/catkin_ws/src/tb3_cleaner/setup.py" \
     \
    build --build-base "/home/dody3333/catkin_ws/build/tb3_cleaner" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/dody3333/catkin_ws/install" --install-scripts="/home/dody3333/catkin_ws/install/bin"
