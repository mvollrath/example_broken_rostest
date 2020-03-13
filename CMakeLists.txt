cmake_minimum_required(VERSION 2.8.3)
project(example_broken_rostest)

find_package(catkin REQUIRED COMPONENTS
  rostest
)

catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

if (CATKIN_ENABLE_TESTING)
  find_package(rostest REQUIRED)
  add_rostest(test/test_flush.test)
endif()
