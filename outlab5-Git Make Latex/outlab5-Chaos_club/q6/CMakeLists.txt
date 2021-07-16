project(outlab5 C CXX)
cmake_minimum_required(VERSION 3.10.2)

include_directories("${PROJECT_SOURCE_DIR}")
add_executable(helloworld ${PROJECT_SOURCE_DIR}/helloworld.cpp)

FIND_PACKAGE(Threads REQUIRED)
add_executable(usespthread ${PROJECT_SOURCE_DIR}/usespthread.cpp)
TARGET_LINK_LIBRARIES(usespthread ${CMAKE_THREAD_LIBS_INIT})

ADD_LIBRARY(MyEngineStatic STATIC ${CMAKE_SOURCE_DIR}/myengine/myengine.cpp)

ADD_LIBRARY(MyEngineDynamic SHARED ${CMAKE_SOURCE_DIR}/myengine/myengine.cpp)
set_target_properties(MyEngineDynamic PROPERTIES PUBLIC_HEADER ${CMAKE_SOURCE_DIR}/myengine/myengine.hpp)

install (TARGETS MyEngineStatic MyEngineDynamic
         ARCHIVE DESTINATION /usr/local/lib
         LIBRARY DESTINATION /usr/local/lib)

INSTALL(FILES ${CMAKE_SOURCE_DIR}/myengine/myengine.hpp DESTINATION /usr/local/include)


