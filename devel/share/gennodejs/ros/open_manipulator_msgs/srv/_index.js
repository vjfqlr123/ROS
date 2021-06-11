
"use strict";

let GetKinematicsPose = require('./GetKinematicsPose.js')
let SetActuatorState = require('./SetActuatorState.js')
let SetDrawingTrajectory = require('./SetDrawingTrajectory.js')
let GetJointPosition = require('./GetJointPosition.js')
let SetJointPosition = require('./SetJointPosition.js')
let SetKinematicsPose = require('./SetKinematicsPose.js')

module.exports = {
  GetKinematicsPose: GetKinematicsPose,
  SetActuatorState: SetActuatorState,
  SetDrawingTrajectory: SetDrawingTrajectory,
  GetJointPosition: GetJointPosition,
  SetJointPosition: SetJointPosition,
  SetKinematicsPose: SetKinematicsPose,
};
