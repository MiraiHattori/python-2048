cmake_minimum_required(VERSION 3.0)

project(game_2048)

set(PYBIND11_CPP_STANDARD -std=c++14)
set(CMAKE_CXX_FLAGS "-Wall -Wextra -O3")

add_subdirectory(pybind11)

file(GLOB MAIN_SOURCES ${CMAKE_CURRENT_LIST_DIR} *.cpp)
set(MAIN_SOURCE_DIR ai board config game util)
foreach(source_dir IN LISTS MAIN_SOURCE_DIR)
    file(GLOB dir_sources ${CMAKE_CURRENT_LIST_DIR} ${source_dir}/*.cpp)
    set(MAIN_SOURCES ${MAIN_SOURCES} ${dir_sources})
endforeach()
include_directories(${CMAKE_CURRENT_LIST_DIR})
pybind11_add_module(game MODULE ${MAIN_SOURCES})
