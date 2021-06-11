// Generated by gencpp from file bebop_msgs/Ardrone3MediaStreamingStateVideoEnableChanged.msg
// DO NOT EDIT!


#ifndef BEBOP_MSGS_MESSAGE_ARDRONE3MEDIASTREAMINGSTATEVIDEOENABLECHANGED_H
#define BEBOP_MSGS_MESSAGE_ARDRONE3MEDIASTREAMINGSTATEVIDEOENABLECHANGED_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace bebop_msgs
{
template <class ContainerAllocator>
struct Ardrone3MediaStreamingStateVideoEnableChanged_
{
  typedef Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> Type;

  Ardrone3MediaStreamingStateVideoEnableChanged_()
    : header()
    , enabled(0)  {
    }
  Ardrone3MediaStreamingStateVideoEnableChanged_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , enabled(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint8_t _enabled_type;
  _enabled_type enabled;



  enum {
    enabled_enabled = 0u,
    enabled_disabled = 1u,
    enabled_error = 2u,
  };


  typedef boost::shared_ptr< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> const> ConstPtr;

}; // struct Ardrone3MediaStreamingStateVideoEnableChanged_

typedef ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<std::allocator<void> > Ardrone3MediaStreamingStateVideoEnableChanged;

typedef boost::shared_ptr< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged > Ardrone3MediaStreamingStateVideoEnableChangedPtr;
typedef boost::shared_ptr< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged const> Ardrone3MediaStreamingStateVideoEnableChangedConstPtr;

// constants requiring out of line definition

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace bebop_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'bebop_msgs': ['/home/dody3333/catkin_ws/src/bebop_autonomy/bebop_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4647d465f8e97fd2dcb5f7341b70a007";
  }

  static const char* value(const ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4647d465f8e97fd2ULL;
  static const uint64_t static_value2 = 0xdcb5f7341b70a007ULL;
};

template<class ContainerAllocator>
struct DataType< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bebop_msgs/Ardrone3MediaStreamingStateVideoEnableChanged";
  }

  static const char* value(const ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Ardrone3MediaStreamingStateVideoEnableChanged\n\
# auto-generated from up stream XML files at\n\
#   github.com/Parrot-Developers/libARCommands/tree/master/Xml\n\
# To check upstream commit hash, refer to last_build_info file\n\
# Do not modify this file by hand. Check scripts/meta folder for generator files.\n\
#\n\
# SDK Comment: Video stream state.\n\
\n\
Header header\n\
\n\
# Current video streaming status.\n\
uint8 enabled_enabled=0  # Video streaming is enabled.\n\
uint8 enabled_disabled=1  # Video streaming is disabled.\n\
uint8 enabled_error=2  # Video streaming failed to start.\n\
uint8 enabled\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.enabled);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Ardrone3MediaStreamingStateVideoEnableChanged_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::bebop_msgs::Ardrone3MediaStreamingStateVideoEnableChanged_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "enabled: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.enabled);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BEBOP_MSGS_MESSAGE_ARDRONE3MEDIASTREAMINGSTATEVIDEOENABLECHANGED_H
