project(outlab51 C CXX)
cmake_minimum_required(VERSION 3.10.2)


SET(APP_EXE mygamestatic)
ADD_EXECUTABLE(${APP_EXE} mygame.cpp)
TARGET_LINK_LIBRARIES(${APP_EXE} /usr/local/lib/libMyEngineStatic.a)

SET(APPI_EXE mygamedynamic)
ADD_EXECUTABLE(${APPI_EXE} mygame.cpp)
TARGET_LINK_LIBRARIES(${APPI_EXE} /usr/local/lib/libMyEngineDynamic.so)