
## Adding color and anchor

Let's add some colors, for a change, let's use different colors than Orange and Red/Blue.

```xml
<!-- Robot name above -->
<gazebo reference="base_link">
	<material>Gazebo/Yellow</material>
</gazebo>

<gazebo reference="prism_arm_link">
	<material>Gazebo/Green</material>
</gazebo>

<link name="world" />

<joint name="world_joint" type="fixed">
	<origin xyz="0 0 0" rpy="0 0 0" />
	<parent link="world" />
	<child link="base_link" />
</joint>
<!-- base_link below  -->
```

## Limits and dynamics

Our limits are mostly blank, so let's add some effort and velocity limits. Let's also add some `dynamics` same time.

```xml
<limit lower="0" upper="2.69" effort="1000" velocity="0.02" />
<dynamics damping="1" friction="0.7" />
```

The speed is slow, so that we can see the movement.

## Transmission and Gazebo plugin

Now, let's add transmission to control the position of the arm.

```xml
<transmission name="prism_arm_trans" type="SimpleTransmission">
	<type>transmission_interface/SimpleTransmission</type>
	<actuator name="prism_arm_motor" />
	<joint name="prism_arm_joint">
		<hardwareInterface>hardware_interface/EffortJointInterface</hardwareInterface>
	</joint>
</transmission>

<gazebo>
	<plugin name="gazebo_ros_control" filename="libgazebo_ros_control.so">
		<robotNamespace>/example_4</robotNamespace>
	</plugin>
</gazebo>
```

## Joint configuration

Let's edit the `joint_names_example_4.yaml` and add this to the end of the file.

```yaml
example_4:
  joint_state_controller:
    type: joint_state_controller/JointStateController
    publish_rate: 20

  arm_controller:
    type: effort_controllers/JointPositionController
    joint: prism_arm_joint
    pid: { p: 100.0, i: 10.0, d: 0.1 }
```

## Gazebo launch

Add these lines to the end of `gazebo.launch`

```xml
<param name="robot_description" textfile="$(find example_4)/urdf/example_4.urdf" />
<rosparam file="$(find example_4)/config/joint_names_example_4.yaml" command="load" />
<node name="controller_spawner" pkg="controller_manager" type="spawner" ns="/example_4" args="joint_state_controller arm_controller" />
```

Let's compile and run a test, then we can do some `GUI` controlling.
