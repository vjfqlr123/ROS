// Generated by gencpp from file dynamixel_workbench_msgs/DynamixelStateList.msg
// DO NOT EDIT!


#ifndef DYNAMIXEL_WORKBENCH_MSGS_MESSAGE_DYNAMIXELSTATELIST_H
#define DYNAMIXEL_WORKBENCH_MSGS_MESSAGE_DYNAMIXELSTATELIST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <dynamixel_workbench_msgs/DynamixelState.h>

namespace dynamixel_workbench_msgs
{
template <class ContainerAllocator>
struct DynamixelStateList_
{
  typedef DynamixelStateList_<ContainerAllocator> Type;

  DynamixelStateList_()
    : dynamixel_state()  {
    }
  DynamixelStateList_(const ContainerAllocator& _alloc)
    : dynamixel_state(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector< ::dynamixel_workbench_msgs::DynamixelState_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::dynamixel_workbench_msgs::DynamixelState_<ContainerAllocator> >::other >  _dynamixel_state_type;
  _dynamixel_state_type dynamixel_state;





  typedef boost::shared_ptr< ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator> const> ConstPtr;

}; // struct DynamixelStateList_

typedef ::dynamixel_workbench_msgs::DynamixelStateList_<std::allocator<void> > DynamixelStateList;

typedef boost::shared_ptr< ::dynamixel_workbench_msgs::DynamixelStateList > DynamixelStateListPtr;
typedef boost::shared_ptr< ::dynamixel_workbench_msgs::DynamixelStateList const> DynamixelStateListConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace dynamixel_workbench_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'dynamixel_workbench_msgs': ['/home/dody3333/catkin_ws/src/dynamixel-workbench-msgs/dynamixel_workbench_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator> >
{
  static const char* value()
  {
    return "52c1af7cbc10f50d2e78a86519b081ee";
  }

  static const char* value(const ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x52c1af7cbc10f50dULL;
  static const uint64_t static_value2 = 0x2e78a86519b081eeULL;
};

template<class ContainerAllocator>
struct DataType< ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dynamixel_workbench_msgs/DynamixelStateList";
  }

  static const char* value(const ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# DynamixelState List\n\
\n\
DynamixelState[] dynamixel_state\n\
\n\
================================================================================\n\
MSG: dynamixel_workbench_msgs/DynamixelState\n\
# This message includes basic data of dynamixel\n\
\n\
string name\n\
uint8  id\n\
\n\
int32  present_position\n\
int32  present_velocity\n\
int16  present_current\n\
\n\
\n\
\n\
";
  }

  static const char* value(const ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.dynamixel_state);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct DynamixelStateList_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::dynamixel_workbench_msgs::DynamixelStateList_<ContainerAllocator>& v)
  {
    s << indent << "dynamixel_state[]" << std::endl;
    for (size_t i = 0; i < v.dynamixel_state.size(); ++i)
    {
      s << indent << "  dynamixel_state[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::dynamixel_workbench_msgs::DynamixelState_<ContainerAllocator> >::stream(s, indent + "    ", v.dynamixel_state[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // DYNAMIXEL_WORKBENCH_MSGS_MESSAGE_DYNAMIXELSTATELIST_H
