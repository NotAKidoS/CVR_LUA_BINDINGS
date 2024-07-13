# CVRLuaModule

## Constructors:

## Enums:

## Wrappers:

# CVR_CCKLuaModule

## Constructors:
- NewCVRAdvancedAvatarSettingsTriggerTask()
- NewCVRAdvancedAvatarSettingsTriggerTaskStay()
- NewCVRAvatarAdvancedTaggingEntry()
- NewCVRAvatarCollider()
- NewCVRDistanceLodGroup()
- NewCVRInteractableActionData()
- NewCVRObjectCatalogCategory()
- NewCVRObjectCatalogEntry()
- NewCVRSpawnableMenuValue()
- NewCVRSpawnableSubSync()
- NewCVRSpawnableValue()

## Enums:
- ActionType
- TrackerType
- BodyMask
- AttachmentType
- ReferenceType
- SampleDirection
- AnimatorType
- Type
- PropPrivacy
- ActionRegister
- InteractionInputModifier
- AudioDataType
- Tags
- RespawnBehavior
- BoneType
- TaskType
- AssetType
- InteractionInput
- ExecutionType
- CVRAvatarVoiceParent
- GripType
- SpawnableType
- UpdateMethod
- InteractionFilter

## Wrappers:
### CVRCustomRenderTextureUpdater
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `customRenderTexture` | `CustomRenderTexture (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AnimatorDriver
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `EnterTasks` | `List<AnimatorDriverTask>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ExitTasks` | `List<AnimatorDriverTask>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localOnly` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerSetup` | `PlayerSetup (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `puppetMaster` | `PuppetMaster (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spawnable` | `CVRSpawnable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `OnStateEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateIK` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateIK` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMachineEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMachineEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMachineExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMachineExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMove` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMove` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateUpdate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateUpdate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### SnappingReference
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `allowedType` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `distance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `point` | `CVRSnappingPoint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `referencePoint` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `target` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRBaseLuaBehaviour
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Globals` | `Table` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Hash` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HashBytes` | `ReadOnlyCollection<byte>` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `InstanceIDBytes` | `ReadOnlyCollection<byte>` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsScriptInitialized` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PathArray` | `ReadOnlyCollection<string>` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ScriptName` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TypeLabel` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CallReceiverFunction` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Crash` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Destroy` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetGlobalString` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetGlobalTable` | `Table` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetObjectID` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetOwnerID` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPath` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AnimatorDriverTask
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `aMax` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `aName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `aValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bMax` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Execute` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRSpawnableTriggerTaskStay
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `maxValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `settingIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spawnable` | `CVRSpawnable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `trigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRDistanceLod
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `distance3D` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Groups` | `List<CVRDistanceLodGroup>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRToggleStatePointer
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `isInternalPointer` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isLocalPointer` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `parentSpawnable` | `CVRSpawnable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pickup` | `CVRPickupObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `type` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRPointer
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `isInternalPointer` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isLocalPointer` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `parentSpawnable` | `CVRSpawnable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pickup` | `CVRPickupObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `type` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRBlitter
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `blitMaterial` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `clearEveryFrame` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `destinationTexture` | `RenderTexture (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `originTexture` | `RenderTexture (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ScoreBoardDisplayElementsTeam
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `playerLists` | `List<Text>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `teamScore` | `List<Text>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRParameterStreamEntry
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `parameterName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `parameterType` | `AnimatorControllerParameterType (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `staticValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `staticValue2` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `staticValue3` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `staticValue4` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `target` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Start` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### PlayerMaterialParser
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `playerChestPositions` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerHeadPositions` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerHipPositions` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerLeftFootPositions` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerLeftHandPositions` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerRightFootPositions` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerRightHandPositions` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerRootPositions` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetMaterial` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Interactable
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AllowMultipleInteractions` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CanInteract` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HoveringRay` | `ControllerRay (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `InteractingRay` | `ControllerRay (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsHovering` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsInteractable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsInteracting` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `IsInteractableWithinRange` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRCameraHelper
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `cam` | `Camera` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `replacementShaders` | `List<Shader>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `selectedShader` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `setAsMirroringCamera` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `TakeScreenshot` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRFaceTracking
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `BlendShapeStrength` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `BlendShapeValues` | `float[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableOverdriveBlendShapes` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FaceBlendShapes` | `string[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FaceMesh` | `SkinnedMeshRenderer` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isLocal` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LipSyncWasUpdated` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UseFacialTracking` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRObjectSync
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `guid` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isPhysicsSynced` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `syncedBy` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SyncedByMe` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `syncOwner` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SyncType` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tasks` | `List<CVRObjectSyncTask>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `getInitialObject` | `CVRSerializableObjectSync (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `getInitialTaskData` | `CVRSerializableObjectSyncTask[] (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRSpawnableSubSync
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `syncBoundary` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ScoreBoardController
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `gameInstanceController` | `GameInstanceController` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `roundStatus` | `List<Text>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `roundTimers` | `List<Text>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `teamElements` | `List<ScoreBoardDisplayElementsTeam>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRInteractableAction
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `additionalData` | `CVRInteractableActionData` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `allowedPointer` | `List<CVRPointer>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `allowedPointerCollapse` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `allowedTypes` | `List<string>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `allowedTypesCollapse` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `boolVal` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `boolVal2` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `delay` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `floatVal` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `floatVal2` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `floatVal3` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `guid` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `layerMask` | `LayerMask` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `operations` | `List<CVRInteractableActionOperation>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `parentInteractable` | `CVRInteractable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `recievedSyncGuids` | `string[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `specificParticleSystems` | `List<ParticleSystem>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `specificParticleSystemsCollapse` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stringVal` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `syncGuids` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `syncGuidsIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `testVal` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `varBufferVal` | `CVRVariableBuffer` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `varBufferVal2` | `CVRVariableBuffer` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Health
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `armorBaseAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorMaxAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorRegenerationCap` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorRegenerationDelay` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorRegenerationRate` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorRegenerationTimer` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentArmor` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentHealth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentShield` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `damageReceivedEvent` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthBaseAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthMaxAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthRegenerationCap` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthRegenerationDelay` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthRegenerationRate` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthRegenerationTimer` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isDown` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `referenceID` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldBaseAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldMaxAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldRegenerationCap` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldRegenerationDelay` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldRegenerationRate` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldRegenerationTimer` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ApplyDamageFromLocation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DealDamage` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DealDamage` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DealDamage` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DealDamageOverTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Down` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Down` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnParticleCollisionEv` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetDamageTimers` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRParticleSound
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `dieAudioSourceReference` | `AudioSource` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `diePlaybackVolume` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `dieSound` | `AudioClip[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `simulateSpeedOfSound` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spawnAudioSourceReference` | `AudioSource` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spawnPlaybackVolume` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spawnSound` | `AudioClip[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRAssetInfo
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `cckVersion` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `objectId` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `unityVersion` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRAvatar
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `advancedTaggingList` | `ReadOnlyCollection<CVRAvatarAdvancedTaggingEntry>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AssetInfo` | `CVRAssetInfo` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `avatarColliders` | `ReadOnlyCollection<CVRAvatarCollider>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `avatarSettings` | `CVRAdvancedAvatarSettings (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `avatarUsesAdvancedSettings` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `blinkBlendshape` | `ReadOnlyCollection<string>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `blinkDuration` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `blinkGap` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bodyMesh` | `SkinnedMeshRenderer` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableAdvancedTagging` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `EyeMovementController` | `EyeMovementController (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `eyeMovementInterval` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `faceTrackingComponents` | `ReadOnlyCollection<CVRFaceTracking>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `leftGrabPointer` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `leftIndexPointer` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `materials` | `ReadOnlyCollection<Material>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mouthPointer` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `overrides` | `AnimatorOverrideController` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderTextures` | `ReadOnlyCollection<RenderTexture> (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rightGrabPointer` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rightIndexPointer` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useBlinkBlendshapes` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useEyeMovement` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useVisemeLipsync` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `viewPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `visemeBlendshapes` | `ReadOnlyCollection<string>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `VisemeController` | `CVRLipSyncManager (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `visemeSmoothing` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `voicePosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetViewRelativePosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetViewWorldPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetVoiceWorldPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRSpawnableValue
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `animator` | `Animator` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameterName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `startValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRBuilderSpawnable
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `allowGenerateTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `guid` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `instanceId` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRDistanceConstrain
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `maxDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `target` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRSnappingPoint
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `distance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `type` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRObjectCatalogCategory
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `id` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `image` | `Texture2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRInteractableActionOperation
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `animationVal` | `AnimationClip` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `boolVal` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `boolVal2` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `customEvent` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `floatVal` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `floatVal2` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `floatVal3` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `floatVal4` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObjectVal` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `parentInteractable` | `CVRInteractable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stringVal` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stringVal2` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stringVal3` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stringVal4` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targets` | `List<GameObject>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `varBufferVal` | `CVRVariableBuffer` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `varBufferVal2` | `CVRVariableBuffer` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `varBufferVal3` | `CVRVariableBuffer` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRLuaClientBehaviour
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `TypeLabel` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Globals` | `Table` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Hash` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HashBytes` | `ReadOnlyCollection<byte>` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `InstanceIDBytes` | `ReadOnlyCollection<byte>` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsScriptInitialized` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PathArray` | `ReadOnlyCollection<string>` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ScriptName` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CallReceiverFunction` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Crash` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Destroy` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetGlobalString` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetGlobalTable` | `Table` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetObjectID` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetOwnerID` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPath` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRInteractable
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `actions` | `List<CVRInteractableAction>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AllowMultipleInteractions` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isAttached` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isHeld` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsInteractable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isLookedAt` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isSitting` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `onEnterSeat` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `onExitSeat` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tooltip` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CanInteract` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HoveringRay` | `ControllerRay (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `InteractingRay` | `ControllerRay (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsHovering` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsInteracting` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Awake` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CustomTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsInteractableWithinRange` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnBecameInvisible` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnBecameVisible` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnCollisionEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnCollisionExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnDestroy` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnDisable` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnEnable` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnParticleCollision` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnTriggerEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnTriggerExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Start` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Update` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRAvatarCollider
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `collider` | `Collider` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRGlobalMaterialPropertyUpdater
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `floatValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `floatValueAnimatable` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `integerValue` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `integerValueAnimatable` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `intValue` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `intValueAnimatable` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `propertyName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `vector4Value` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `vector4ValueAnimatable` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ControlPoint
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `captureBonusForMultiplePeople` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `captureTime` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameInstanceController` | `GameInstanceController` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `recaptureDelay` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `referenceID` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `scorePerSecond` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRHapticZone
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `bounds` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `center` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableOnEnter` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableOnExit` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableOnStay` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `onEnterIntensity` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `onExitIntensity` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `onStayChance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `onStayIntensity` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRAvatarAdvancedTaggingEntry
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `fallbackGameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### GameInstanceController
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `autoBalanceTeams` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `balanceTeamJoin` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `endScore` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `endTime` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameEnded` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameStarted` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `readyPercentage` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `readyTimer` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `referenceID` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `roundEnded` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `roundStarted` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `roundsToWin` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ScoreBoardControllers` | `List<ScoreBoardController>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `teams` | `List<Team> (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useTeams` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `EnemyScore` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GameEnded` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GameStarted` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `JoinTeamAutoBalance` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LeaveTeam` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OwnScore` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RoundEnded` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RoundStarted` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `StartGame` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToggleReady` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TryJoinTeam` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateStatus` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateTeamList` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateTeamScores` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### GravityZone
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `center` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gravityFalloff` | `AnimationCurve` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerGravityCustomAlignmentValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `priority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `size` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Strength` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `EnterCollider` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ExitCollider` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ShouldAffect` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### FluidVolume
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `density` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `depth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `extend` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `placeFromCenter` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `splashParticleSystem` | `ParticleSystem` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `streamAngle` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `streamStrength` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CreateSplash` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetMainCollider` | `Collider` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetStreamForce` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsInside` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsMainTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRMaterialDriver
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `material01W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material01X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material01Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material01Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material02W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material02X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material02Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material02Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material03W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material03X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material03Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material03Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material04W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material04X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material04Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material04Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material05W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material05X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material05Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material05Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material06W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material06X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material06Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material06Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material07W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material07X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material07Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material07Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material08W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material08X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material08Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material08Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material09W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material09X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material09Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material09Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material10W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material10X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material10Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material10Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material11W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material11X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material11Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material11Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material12W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material12X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material12Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material12Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material13W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material13X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material13Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material13Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material14W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material14X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material14Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material14Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material15W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material15X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material15Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material15Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material16W` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material16X` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material16Y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material16Z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tasks` | `List<CVRMaterialDriverTask>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### SpawnablePickupMarker
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `spawnableGuid` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `SelectSpawnableForSpawn` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ShowSpawnableDetailsPage` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRMaterialDriverTask
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Index` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PropertyName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Renderer` | `Renderer` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RendererType` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `values` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `SetValue` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRAudioDriver
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `audioClips` | `List<AudioClip>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `audioSource` | `AudioSource` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playOnSwitch` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `selectedAudioClip` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `PlayNext` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlayPrev` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlaySound` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlaySound` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SelectRandomSound` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRMovementParent
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `applyForcesFromPlayers` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fixedVelocity` | `Vector3` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRAdvancedAvatarSettingsPointer
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `isInternalPointer` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isLocalPointer` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `parentSpawnable` | `CVRSpawnable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pickup` | `CVRPickupObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `type` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### BodyControl
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `EnterTasks` | `List<BodyControlTask>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ExitTasks` | `List<BodyControlTask>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `OnStateEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateIK` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateIK` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMachineEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMachineEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMachineExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMachineExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMove` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMove` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateUpdate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateUpdate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRObjectLibrary
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `objectCatalogCategories` | `List<CVRObjectCatalogCategory>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `objectCatalogEntries` | `List<CVRObjectCatalogEntry>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRAdvancedAvatarSettingsTrigger
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `allowedPointer` | `List<CVRPointer>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `allowedTypes` | `string[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `allowParticleInteraction` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `areaOffset` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `areaSize` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enterTasks` | `List<CVRAdvancedAvatarSettingsTriggerTask>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `exitTasks` | `List<CVRAdvancedAvatarSettingsTriggerTask>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isLocalInteractable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isNetworkInteractable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `settingName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `settingValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stayTasks` | `List<CVRAdvancedAvatarSettingsTriggerTaskStay>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useAdvancedTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `EnterTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `EnterTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `EnterTriggerParticle` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ExitTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ExitTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ExitTriggerParticle` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `StayTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Trigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRAdvancedAvatarSettingsTriggerHelper
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `triggers` | `List<CVRAdvancedAvatarSettingsTrigger>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `onEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `onExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `onStay` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRDistanceLodGroup
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MaxDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MinDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRMirror
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `m_ClipPlaneOffset` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m_CustomColor` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m_CustomSkybox` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m_DisablePixelLights` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m_framesNeededToUpdate` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m_ignoreLegacyBehaviour` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m_ReflectLayers` | `LayerMask` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m_TextureSize` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m_UseOcclusionCulling` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetMirrorReflectionPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `settingsChanged` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### PhysicsInfluencer
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `airAngularDrag` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `airDrag` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `centerOfMass` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `density` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableBuoyancy` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableInfluence` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableLocalGravity` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fluidAngularDrag` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fluidDrag` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forceAlignUpright` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `volume` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetAppliedGravity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetAppliedGravityDirection` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetDepth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetSubmerged` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTimeSinceEnter` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTimeSinceExit` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateDensity` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRToggleStateTrigger
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `areaOffset` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `areaSize` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `toggleStateID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Trigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CombatSystem
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `DefaultDeathAnimation` | `AnimationClip` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `downedAnotherPlayerEvent` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `friendlyFire` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hitAnotherPlayerEvent` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerDownedEvent` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerDownEvent` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerGotHitEvent` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerHitEvent` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerRespawnEvent` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerRevitalizeEvent` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `respawnPoint` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `respawnTime` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorBaseAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorMaxAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorRegenerationCap` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorRegenerationDelay` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorRegenerationRate` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorRegenerationTimer` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentArmor` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentHealth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentShield` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `damageReceivedEvent` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthBaseAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthMaxAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthRegenerationCap` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthRegenerationDelay` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthRegenerationRate` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthRegenerationTimer` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isDown` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `referenceID` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldBaseAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldMaxAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldRegenerationCap` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldRegenerationDelay` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldRegenerationRate` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldRegenerationTimer` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Down` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RespawnIfNecessary` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ApplyDamageFromLocation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DealDamage` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DealDamage` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DealDamage` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DealDamageOverTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Down` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnParticleCollisionEv` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetDamageTimers` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRSpawnable
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `currentIncomingSubSyncFloats` | `ReadOnlyCollection<float>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `customData` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `guid` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `instanceId` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isPhysicsSynced` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ownerId` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preGeneratedInstanceId` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spawnHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `subSyncs` | `List<CVRSpawnableSubSync>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SyncType` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `syncValues` | `List<CVRSpawnableValue>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useAdditionalValues` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `usedParametersForSubSync` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ForceUpdate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ForceUpdate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsMine` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsSyncedByMe` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetValue` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateMultiPurposeFloat` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateValueIfNecessary` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRObjectCatalogEntry
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `categoryId` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `guid` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `prefab` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preview` | `Texture2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Damage
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `armorMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `damageAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `damageOverTimeAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `damageOverTimeContact` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `damageOverTimeDuration` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableFalloff` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `falloffCurve` | `AnimationCurve` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `falloffDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `falloffEffectDamageOverTime` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRAction
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `actionName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `actionObjects` | `ReadOnlyCollection<GameObject>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRAudioMaterialParser
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `distanceParameterName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `dopplerParameterName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fragmentParameterNameL1` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fragmentParameterNameL2` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fragmentParameterNameL3` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fragmentParameterNameL4` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fragmentParameterNameR1` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fragmentParameterNameR2` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fragmentParameterNameR3` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fragmentParameterNameR4` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fragmentSize` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pitchParameterName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `processingMaterial` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sourceAudio` | `AudioSource` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sourceAudioL` | `AudioSource` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sourceAudioR` | `AudioSource` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spatialParameterName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useSeparateAudioSources` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `volumeParameterName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRAttachment
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `maxAttachmentDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `onAttach` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `onDeattach` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `positionOffset` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rotationOffset` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `snappingPointTypes` | `ReadOnlyCollection<string>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useFixedPositionOffset` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useFixedRotationOffset` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Attach` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DeAttach` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsAttached` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRAnimatorDriver
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `animatorParameter01` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameter02` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameter03` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameter04` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameter05` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameter06` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameter07` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameter08` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameter09` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameter10` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameter11` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameter12` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameter13` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameter14` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameter15` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameter16` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameters` | `List<string>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorParameterType` | `List<int>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animators` | `List<Animator>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRAdvancedAvatarSettingsTriggerTask
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `delay` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `holdTime` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `settingName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `settingValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ClearSchedulerJob` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ExecuteTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Trigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Trigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TriggerDelayed` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Update` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRSpawnableTrigger
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `allowedTypes` | `string[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `allowParticleInteraction` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `areaOffset` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `areaSize` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enterTasks` | `List<CVRSpawnableTriggerTask>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `exitTasks` | `List<CVRSpawnableTriggerTask>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `settingIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `settingValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stayTasks` | `List<CVRSpawnableTriggerTaskStay>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useAdvancedTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `EnterTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `EnterTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `EnterTriggerParticle` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ExitTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ExitTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ExitTriggerParticle` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `StayTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Trigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRHapticAreaChest
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `chestAreaSize` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### BodyControlTask
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `isBlend` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetWeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transitionDuration` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Execute` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### BoundObject
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `boundThing` | `UnityObject` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRSpawnableTriggerTask
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `delay` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `holdTime` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `settingIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `settingValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spawnable` | `CVRSpawnable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ClearSchedulerJob` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ExecuteTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Trigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Trigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TriggerDelayed` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Update` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRNavController
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `navMeshAgent` | `NavMeshAgent` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `navTargetIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `navTargetList` | `Transform[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `patrolEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `patrolPointCheckDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `patrolPointIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `patrolPoints` | `Transform[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRPortalMarker
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `worldGUID` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRInteractableActionData
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `floats` | `List<float>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `set` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `variableBufferValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Reset` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ObjectHealth
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `connectedGameInstance` | `GameInstanceController` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `downEvent` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `respawnEvent` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `respawnPoint` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `respawnTime` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorBaseAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorMaxAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorRegenerationCap` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorRegenerationDelay` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorRegenerationRate` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `armorRegenerationTimer` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentArmor` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentHealth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentShield` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `damageReceivedEvent` | `UnityEvent (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthBaseAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthMaxAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthRegenerationCap` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthRegenerationDelay` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthRegenerationRate` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `healthRegenerationTimer` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isDown` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `referenceID` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldBaseAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldMaxAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldRegenerationCap` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldRegenerationDelay` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldRegenerationRate` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shieldRegenerationTimer` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Down` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ApplyDamageFromLocation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DealDamage` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DealDamage` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DealDamage` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DealDamageOverTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Down` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnParticleCollisionEv` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetDamageTimers` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRVariableBuffer
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `defaultValue` | `float` | `CLIENT` | `WORLD` | `ANY` | `ANY` |
| `value` | `float` | `CLIENT` | `WORLD` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `WORLD` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `WORLD` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `WORLD` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `WORLD` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `WORLD` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `WORLD` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `SetValue` | `void` | `ANY` | `WORLD` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `WORLD` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `WORLD` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `WORLD` | `ANY` | `ANY` |
### CVRSpawnableMenuValue
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `value` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### GunController
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ammoCapacity` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `emptyShootSounds` | `List<AudioClip>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `firingRate` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hitMask` | `LayerMask` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lastPlayerFired` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `magazineSize` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `referenceID` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reloadSounds` | `List<AudioClip>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reloadTime` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shootSounds` | `List<AudioClip>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `executeNetworkFire` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ExecuteReload` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GrantMagazineAmmo` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GrantReserveAmmo` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Reload` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Shoot` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ShootDown` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ShootUp` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRPickupObject
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `autoHold` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CanPickup` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `disallowTheft` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DisallowTheft` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gripOrigin` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ikReference` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsAutoHold` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsObjectInteractionAllowed` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsObjectPushPullAllowed` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsObjectRotationAllowed` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MaxGrabDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maximumGrabDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MaxPushDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RootTransform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `snappingReferences` | `List<SnappingReference>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `teleTargetObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `updateWithPhysics` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ControllerRay` | `ControllerRay (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsGrabbedByMe` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsPickedUp` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsPickupable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetTimeSinceGrabStart` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetFlungStatus` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetLocation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetWasUsingGravity` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsWithinGrabReach` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRGlobalShaderUpdater
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CVR_CCK_Global_1` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CVR_CCK_Global_2` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CVR_CCK_Global_3` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CVR_CCK_Global_4` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `propertyName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderTexture` | `RenderTexture (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `updateTexture` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `updateValues` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRMaterialUpdater
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Pickupable
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CanPickup` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ControllerRay` | `ControllerRay (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DisallowTheft` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsAutoHold` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsGrabbedByMe` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsObjectInteractionAllowed` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsObjectPushPullAllowed` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsObjectRotationAllowed` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsPickedUp` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsPickupable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MaxGrabDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MaxPushDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RootTransform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `IsWithinGrabReach` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRParameterStream
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `attachment` | `CVRAttachment` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `avatar` | `CVRAvatar` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `entries` | `ReadOnlyCollection<CVRParameterStreamEntry>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `influencer` | `PhysicsInfluencer` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `objectSync` | `CVRObjectSync` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `onlyUpdateWhenAttached` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `onlyUpdateWhenControlled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `onlyUpdateWhenHeld` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pickup` | `CVRPickupObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `seat` | `CVRSeat (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spawnable` | `CVRSpawnable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRAvatarPickupMarker
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `avatarGuid` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ChangeAvatar` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ShowAvatarDetailsPage` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ForceApplicator
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `forceVector` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `onlyWhenSubmerged` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `strength` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `target` | `Rigidbody` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRObjectSyncTask
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `component` | `Component` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `intVal` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CVRAdvancedAvatarSettingsTriggerTaskStay

# CVR_NetworkLuaModule

## Constructors:

## Enums:

## Wrappers:
### IncomingScriptNetworkMessage
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AddressingPolicy` | `ScriptNetworkAddressingPolicy (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `InstanceID` | `ScriptInstanceID (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ScriptID` | `ScriptID (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Sender` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SenderIsLocal` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ShallBroadcast` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TargetInstances` | `ReadOnlyCollection<ScriptInstanceID> (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TargetScripts` | `ReadOnlyCollection<ScriptID> (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ReadBool` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadBoolArray` | `bool[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadByte` | `byte` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadByteArray` | `byte[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadChar` | `char` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadCharArray` | `char[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadDouble` | `double` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadDoubleArray` | `double[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadFloat` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadFloatArray` | `float[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadInt` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadIntArray` | `int[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadLong` | `long` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadLongArray` | `long[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadQuaternion` | `Quaternion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadQuaternionArray` | `Quaternion[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadShort` | `short` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadShortArray` | `short[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadSignedByte` | `sbyte` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadSignedByteArray` | `sbyte[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadStringArray` | `string[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadUnsignedInt` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadUnsignedIntArray` | `uint[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadUnsignedLong` | `ulong` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadUnsignedLongArray` | `ulong[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadUnsignedShort` | `ushort` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadUnsignedShortArray` | `ushort[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadVector3` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadVector3Array` | `Vector3[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### OutgoingScriptNetworkMessage
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `SendTo` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SendToAll` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteBool` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteBoolArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteByte` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteByteArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteChar` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteChar` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteCharArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteCharArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteDouble` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteDoubleArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteFloat` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteFloatArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteInt` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteIntArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteLong` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteLongArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteShort` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteShortArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteSignedByte` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteSignedByteArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteString` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteStringArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteUnsignedInt` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteUnsignedIntArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteUnsignedLong` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteUnsignedLongArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteUnsignedShort` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteUnsignedShortArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |

# RCCLuaModule

## Constructors:
- NewConfigureVehicleSubsteps()
- NewGear()
- NewRCC_AssetPaths()
- NewRCC_Inputs()
- NewRCC_Settings()

## Enums:
- IndicatorsOn
- WheelType
- AudioType
- WheelDamage

## Wrappers:
### RCC_Teleporter
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `spawnPoint` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### RCC_Mirror
### RCC_Camera
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `hoodCameraFOV` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isRendering` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maximumOrtSize` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maximumZDistanceOffset` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxOrbitY` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minimumOrtSize` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minOrbitY` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `occlusionLayerMask` | `LayerMask` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `oldOrbitY` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `orbitReset` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `orbitSmooth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `orbitXSpeed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `orbitYSpeed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pivot` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playerCar` | `RCC_CarControllerV3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `thisCam` | `Camera` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `topCameraAngle` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `topCameraDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TPSAutoFocus` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TPSAutoReverse` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TPSCollision` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TPSDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TPSHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TPSMaximumFOV` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TPSMinimumFOV` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TPSOffset` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TPSPitch` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TPSRotationDamping` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TPSStartRotation` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TPSTiltMaximum` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TPSTiltMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TPSYaw` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useAutoChangeCamera` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useCinematicCameraMode` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useFixedCameraMode` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useHoodCameraMode` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useOcclusion` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useOrbitInHoodCameraMode` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useOrbitInTPSCameraMode` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useOrthoForTopCamera` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useTopCameraMode` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useWheelCameraMode` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wheelCameraFOV` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AutoFocus` | `IEnumerator (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AutoFocus` | `IEnumerator (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AutoFocus` | `IEnumerator (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AutoFocus` | `IEnumerator (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ChangeCamera` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ChangeCamera` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Collision` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnDrag` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnDrag` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemoveTarget` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTarget` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToggleCamera` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### RCC_FuelStation
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `refillSpeed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### RCC_AssetPaths
### RCC_Caliper
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `wheelCollider` | `RCC_WheelCollider (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### RCC_Inputs
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `boostInput` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `brakeInput` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `clutchInput` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gearInput` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `handbrakeInput` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `steerInput` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `throttleInput` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `SetInput` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetInput` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetInput` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetInput` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### RCC_Light
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `defaultIntensity` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flare` | `Flare (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flareBrightness` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `indicatorClip` | `AudioClip` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `inertia` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `refreshRate` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Init` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Gear
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `maxRatio` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxSpeed` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetSpeedForNextGear` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `SetGear` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### RCC_Core
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CreateWheelColliders` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetBehavior` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### RCC_Waypoint
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `targetSpeed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### RCC_RepairStation
### RCC_Exhaust
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `boostFlameColor` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flame` | `ParticleSystem` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flameColor` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flameTime` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flareBrightness` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxEmission` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxSize` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxSpeed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minEmission` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minSize` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minSpeed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `previewFlames` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### RCC
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `WORLD` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `WORLD` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `WORLD` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `WORLD` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `WORLD` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `WORLD` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `WORLD` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `WORLD` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `WORLD` | `ANY` | `ANY` |
### RCC_Settings
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `audioMixer` | `AudioMixerGroup (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `autoReset` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `autoReverse` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `behaviorSelectedIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `blowoutClip` | `AudioClip[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `boostKB` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `brakeClip` | `AudioClip` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `brakeLights` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bumpClip` | `AudioClip` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `changeCameraKB` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `chassisJoint` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cinematicCamera` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `contactParticles` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `controllerSelectedIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `crashClips` | `AudioClip[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `dontUseAnyParticleEffects` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `dontUseSkidmarks` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `exhaustFlameClips` | `AudioClip[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `exhaustGas` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fixedTimeStep` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `foldBehaviorSettings` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `foldControllerSettings` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `foldGeneralSettings` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `foldOptimization` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `foldSFX` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `foldTagsAndLayers` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `foldUISettings` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `foldWheelPhysics` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gearShiftingClips` | `AudioClip[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gyroSensitivity` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `handbrakeKB` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hazardIndicatorKB` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `headLights` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `highBeamHeadlightsKB` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hoodCamera` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `horizontalInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `indicatorClip` | `AudioClip` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `indicatorLights` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `leftIndicatorKB` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightTrailers` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lockAndUnlockCursor` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LogiSteeringWheel_boostKB` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LogiSteeringWheel_changeCameraKB` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LogiSteeringWheel_handbrakeKB` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LogiSteeringWheel_hazardIndicatorKB` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LogiSteeringWheel_highBeamHeadlightsKB` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LogiSteeringWheel_lookBackKB` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LogiSteeringWheel_lowBeamHeadlightsKB` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LogiSteeringWheel_shiftGearDown` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LogiSteeringWheel_shiftGearUp` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LogiSteeringWheel_startEngineKB` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lookBackKB` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lowBeamHeadlightsKB` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxAngularVelocity` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxBrakeSoundVolume` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxCrashSoundVolume` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxFPS` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxGearShiftingSoundVolume` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxWindSoundVolume` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mirrors` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mouseXInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mouseYInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `NGear` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `NOSClip` | `AudioClip` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `overrideBehavior` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `overrideFixedTimeStep` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `overrideFPS` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playbackKB` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `projector` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `projectorIgnoreLayer` | `LayerMask` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_boostKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_changeCameraKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_handbrakeKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_hazardIndicatorKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_highBeamHeadlightsKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_horizontalInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_indicatorKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_lookBackKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_lowBeamHeadlightsKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_mouseXInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_mouseYInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_shiftGearDown` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_shiftGearUp` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_startEngineKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_trailerAttachDetach` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_triggerLeftInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_triggerRightInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PS4_verticalInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RCCCanvas` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RCCLayer` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RCCMainCamera` | `RCC_Camera` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RCCTag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RCCTelemetry` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `recordKB` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reverseLights` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reversingClip` | `AudioClip` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rightIndicatorKB` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `runEngineAtAwake` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `setTagsAndLayers` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shiftGearDown` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shiftGearUp` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `skidmarksManager` | `RCC_SkidmarksManager (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `slowMotionKB` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `startEngineKB` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tagAllChildrenGameobjects` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `trailerAttachDetach` | `KeyCode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `turboClip` | `AudioClip` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UIButtonGravity` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UIButtonSensitivity` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useAutomaticClutch` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useAutomaticGear` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useFixedWheelColliders` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useLightProjectorForLightingEffect` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useLightsAsVertexLights` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useTelemetry` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useVR` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `verticalInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `windClip` | `AudioClip` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_boostKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_changeCameraKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_handbrakeKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_hazardIndicatorKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_highBeamHeadlightsKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_horizontalInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_indicatorKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_lookBackKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_lowBeamHeadlightsKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_mouseXInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_mouseYInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_shiftGearDown` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_shiftGearUp` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_startEngineKB` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_trailerAttachDetach` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_triggerLeftInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_triggerRightInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Xbox_verticalInput` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### RCC_Spawner
### RCC_CarControllerV3
### RCC_SceneManager
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `activeMainCamera` | `Camera` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `activePlayerCamera` | `RCC_Camera` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `activePlayerCanvas` | `RCC_UIDashboardDisplay (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `activePlayerVehicle` | `RCC_CarControllerV3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `allRecorders` | `List<RCC_Recorder> (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `allVehicles` | `List<RCC_CarControllerV3>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `disableUIWhenNoPlayerVehicle` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `loadCustomizationAtFirst` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `registerFirstVehicleAsPlayer` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ChangeCamera` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CheckCanvas` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DeRegisterPlayer` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Play` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Record` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RegisterPlayer` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RegisterPlayer` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RegisterPlayer` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Stop` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Transport` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Transport` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### RCC_Version
### ConfigureVehicleSubsteps
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `speedThreshold` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stepsAboveThreshold` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stepsBelowThreshold` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### RCC_CinematicCamera
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `pivot` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetFOV` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |

# SystemLuaModule

## Constructors:
- NewObject()

## Enums:

## Wrappers:
### ValueType
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Object
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |

# TextMeshProLuaModule

## Constructors:

## Enums:

## Wrappers:
### TMP_Text
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `alignment` | `TextAlignmentOptions (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `alpha` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `autoSizeTextContainer` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `characterSpacing` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `characterWidthAdjustment` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `color` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colorGradient` | `VertexGradient (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colorGradientPreset` | `TMP_ColorGradient (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableAutoSizing` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableCulling` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableKerning` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableVertexGradient` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableWordWrapping` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `extraPadding` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `faceColor` | `Color32` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `firstOverflowCharacterIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `firstVisibleCharacter` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flexibleHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flexibleWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `font` | `TMP_FontAsset (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontMaterial` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontMaterials` | `Material[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontSharedMaterial` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontSharedMaterials` | `Material[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontSize` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontSizeMax` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontSizeMin` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontStyle` | `FontStyles (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontWeight` | `FontWeight (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `geometrySortingOrder` | `VertexSortingOrder (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `havePropertiesChanged` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `horizontalAlignment` | `HorizontalAlignmentOptions (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `horizontalMapping` | `TextureMappingOptions (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ignoreVisibility` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isOrthographic` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isOverlay` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isRightToLeftText` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTextObjectScaleStatic` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTextOverflowing` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTextTruncated` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isUsingBold` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isUsingLegacyAnimationComponent` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isVolumetricText` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `layoutPriority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lineSpacing` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lineSpacingAdjustment` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `linkedTextComponent` | `TMP_Text` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mappingUvLineOffset` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `margin` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxVisibleCharacters` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxVisibleLines` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxVisibleWords` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mesh` | `Mesh (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `outlineColor` | `Color32` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `outlineWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `overflowMode` | `TextOverflowModes (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `overrideColorTags` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pageToDisplay` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `paragraphSpacing` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `parseCtrlCharacters` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pixelsPerUnit` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preferredHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preferredWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rectTransform` | `RectTransform (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderedHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderedWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderMode` | `TextRenderFlags (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `richText` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spriteAsset` | `TMP_SpriteAsset (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `styleSheet` | `TMP_StyleSheet (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `text` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textBounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textInfo` | `TMP_TextInfo (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textPreprocessor` | `ITextPreprocessor (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textStyle` | `TMP_Style (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tintAllSprites` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useMaxVisibleDescender` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `vertexBufferAutoSizeReduction` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `verticalAlignment` | `VerticalAlignmentOptions (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `verticalMapping` | `TextureMappingOptions (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wordSpacing` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wordWrappingRatios` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ClearMesh` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClearMesh` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ComputeMarginSize` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeAlpha` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeColor` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ForceMeshUpdate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetParsedText` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPreferredValues` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPreferredValues` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPreferredValues` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPreferredValues` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetRenderedValues` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetRenderedValues` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTextInfo` | `TMP_TextInfo (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetCharArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetCharArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetVertices` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateGeometry` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateMeshPadding` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateVertexData` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateVertexData` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### TextMeshPro
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `autoSizeTextContainer` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maskType` | `MaskingTypes (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mesh` | `Mesh (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `meshFilter` | `MeshFilter (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderer` | `Renderer` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingLayerID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingOrder` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `alignment` | `TextAlignmentOptions (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `alpha` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `characterSpacing` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `characterWidthAdjustment` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `color` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colorGradient` | `VertexGradient (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colorGradientPreset` | `TMP_ColorGradient (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableAutoSizing` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableCulling` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableKerning` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableVertexGradient` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableWordWrapping` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `extraPadding` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `faceColor` | `Color32` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `firstOverflowCharacterIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `firstVisibleCharacter` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flexibleHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flexibleWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `font` | `TMP_FontAsset (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontMaterial` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontMaterials` | `Material[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontSharedMaterial` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontSharedMaterials` | `Material[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontSize` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontSizeMax` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontSizeMin` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontStyle` | `FontStyles (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontWeight` | `FontWeight (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `geometrySortingOrder` | `VertexSortingOrder (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `havePropertiesChanged` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `horizontalAlignment` | `HorizontalAlignmentOptions (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `horizontalMapping` | `TextureMappingOptions (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ignoreVisibility` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isOrthographic` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isOverlay` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isRightToLeftText` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTextObjectScaleStatic` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTextOverflowing` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTextTruncated` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isUsingBold` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isUsingLegacyAnimationComponent` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isVolumetricText` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `layoutPriority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lineSpacing` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lineSpacingAdjustment` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `linkedTextComponent` | `TMP_Text` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mappingUvLineOffset` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `margin` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxVisibleCharacters` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxVisibleLines` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxVisibleWords` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `outlineColor` | `Color32` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `outlineWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `overflowMode` | `TextOverflowModes (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `overrideColorTags` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pageToDisplay` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `paragraphSpacing` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `parseCtrlCharacters` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pixelsPerUnit` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preferredHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preferredWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rectTransform` | `RectTransform (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderedHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderedWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderMode` | `TextRenderFlags (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `richText` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spriteAsset` | `TMP_SpriteAsset (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `styleSheet` | `TMP_StyleSheet (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `text` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textBounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textInfo` | `TMP_TextInfo (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textPreprocessor` | `ITextPreprocessor (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textStyle` | `TMP_Style (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tintAllSprites` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useMaxVisibleDescender` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `vertexBufferAutoSizeReduction` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `verticalAlignment` | `VerticalAlignmentOptions (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `verticalMapping` | `TextureMappingOptions (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wordSpacing` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wordWrappingRatios` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CalculateLayoutInputHorizontal` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CalculateLayoutInputVertical` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClearMesh` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ComputeMarginSize` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ForceMeshUpdate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTextInfo` | `TMP_TextInfo (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Rebuild` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetAllDirty` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLayoutDirty` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetMask` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetMask` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetMaterialDirty` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetVerticesDirty` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateFontAsset` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateGeometry` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateMeshPadding` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateVertexData` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateVertexData` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClearMesh` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeAlpha` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeColor` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetParsedText` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPreferredValues` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPreferredValues` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPreferredValues` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPreferredValues` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetRenderedValues` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetRenderedValues` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetCharArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetCharArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetText` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetVertices` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |

# UnityEngineLuaModule

## Constructors:
- NewBurst()
- NewBurst()
- NewBurst()
- NewBurst()
- NewBurst()
- NewMinMaxGradient()
- NewMinMaxGradient()
- NewMinMaxGradient()
- NewMinMaxGradient()
- NewAnimationClip()
- NewAnimationCurve()
- NewAnimationCurve()
- NewAnimationEvent()
- NewAnimatorUtility()
- NewAudioRenderer()
- NewAudioSettings()
- NewBoundingSphere()
- NewBoundingSphere()
- NewBounds()
- NewColor()
- NewColor()
- NewColor32()
- NewCompass()
- NewCubemap()
- NewCubemap()
- NewCubemap()
- NewCubemap()
- NewCubemap()
- NewCubemapArray()
- NewCubemapArray()
- NewCubemapArray()
- NewCubemapArray()
- NewCubemapArray()
- NewCubemapArray()
- NewGameObject()
- NewGameObject()
- NewGameObject()
- NewMatrix4x4()
- NewPhysics()
- NewQuaternion()
- NewRect()
- NewRect()
- NewRect()
- NewScriptableObject()
- NewTexture2D()
- NewTexture2D()
- NewTexture2D()
- NewTexture2D()
- NewTexture2D()
- NewTexture2D()
- NewTexture2D()
- NewTexture3D()
- NewTexture3D()
- NewTexture3D()
- NewTexture3D()
- NewTexture3D()
- NewVector2()
- NewVector3()
- NewVector3()
- NewVector3Int()
- NewVector3Int()
- NewVector4()
- NewVector4()
- NewVector4()

## Enums:
- GateFitMode
- ForceMode
- JointProjectionMode
- QueryTriggerInteraction
- HumanBodyBones
- ConfigurableJointMotion
- RotationDriveMode
- AudioReverbPreset

## Wrappers:
### AnimationState
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `blendMode` | `AnimationBlendMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `clip` | `AnimationClip` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `layer` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `length` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `normalizedSpeed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `normalizedTime` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `speed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `time` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `weight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapMode` | `WrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AddMixingTransform` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddMixingTransform` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemoveMixingTransform` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Texture2D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `calculatedMipmapLevel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `desiredMipmapLevel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `format` | `TextureFormat (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ignoreMipmapLimit` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isReadable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `loadedMipmapLevel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `loadingMipmapLevel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minimumMipmapLevel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `requestedMipmapLevel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `streamingMipmaps` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `streamingMipmapsPriority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `vtOnly` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `anisoLevel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `dimension` | `TextureDimension (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `filterMode` | `FilterMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `graphicsFormat` | `GraphicsFormat (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `height` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mipMapBias` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mipmapCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `texelSize` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `updateCount` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `width` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapMode` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapModeU` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapModeV` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapModeW` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Apply` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Apply` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Apply` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClearMinimumMipmapLevel` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClearRequestedMipmapLevel` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Compress` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixel` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixel` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixelBilinear` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixelBilinear` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels` | `Color[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels` | `Color[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels` | `Color[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels` | `Color[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels32` | `Color32[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels32` | `Color32[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetRawTextureData` | `byte[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsRequestedMipmapLevelLoaded` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LoadRawTextureData` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LoadRawTextureData` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PackTextures` | `Rect[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PackTextures` | `Rect[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PackTextures` | `Rect[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadPixels` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ReadPixels` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Reinitialize` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Reinitialize` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Reinitialize` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixel` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixel` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels32` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels32` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels32` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels32` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateExternalTexture` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetNativeTexturePtr` | `IntPtr (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IncrementUpdateCount` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemParticle
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `angularVelocity` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `angularVelocity3D` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatedVelocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `axisOfRotation` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `position` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `randomSeed` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `remainingLifetime` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rotation` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rotation3D` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `startColor` | `Color32` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `startLifetime` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `startSize` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `startSize3D` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `totalVelocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `velocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetCurrentColor` | `Color32` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetCurrentSize` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetCurrentSize3D` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetMeshIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetMeshIndex` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### SphereCollider
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `center` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `radius` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedArticulationBody` | `ArticulationBody (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedRigidbody` | `Rigidbody` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `contactOffset` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasModifiableContacts` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material` | `PhysicMaterial (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `PhysicMaterial (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ClosestPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClosestPointOnBounds` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Material
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `color` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `doubleSidedGI` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabledKeywords` | `LocalKeyword[] (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableInstancing` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `globalIlluminationFlags` | `MaterialGlobalIlluminationFlags (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mainTexture` | `Texture` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mainTextureOffset` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mainTextureScale` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `passCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderQueue` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shader` | `Shader` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shaderKeywords` | `string[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ComputeCRC` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CopyPropertiesFromMaterial` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DisableKeyword` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `EnableKeyword` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindPass` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetColor` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetColor` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetColorArray` | `Color[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetColorArray` | `Color[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetColorArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetColorArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetFloat` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetFloat` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetFloatArray` | `float[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetFloatArray` | `float[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetFloatArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetFloatArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInt` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInt` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInteger` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInteger` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetMatrixArray` | `Matrix4x4[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetMatrixArray` | `Matrix4x4[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetMatrixArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetMatrixArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPassName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShaderPassEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTexture` | `Texture` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTexture` | `Texture` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTextureOffset` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTextureOffset` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTexturePropertyNameIDs` | `int[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTexturePropertyNameIDs` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTexturePropertyNames` | `string[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTexturePropertyNames` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTextureScale` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTextureScale` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetVector` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetVector` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetVectorArray` | `Vector4[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetVectorArray` | `Vector4[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetVectorArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetVectorArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasBuffer` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasBuffer` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasColor` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasColor` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasConstantBuffer` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasConstantBuffer` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasFloat` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasFloat` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasInt` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasInt` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasInteger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasInteger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasMatrix` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasMatrix` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasProperty` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasProperty` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasTexture` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasTexture` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasVector` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasVector` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsKeywordEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Lerp` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetBuffer` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetBuffer` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetBuffer` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetBuffer` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetColor` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetColor` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetColorArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetColorArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetColorArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetColorArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetConstantBuffer` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetConstantBuffer` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetConstantBuffer` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetConstantBuffer` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetFloat` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetFloat` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetFloatArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetFloatArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetFloatArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetFloatArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetInt` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetInt` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetInteger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetInteger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetMatrix` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetMatrix` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetMatrixArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetMatrixArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetMatrixArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetMatrixArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetOverrideTag` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPass` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetShaderPassEnabled` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTexture` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTexture` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTexture` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTexture` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTextureOffset` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTextureOffset` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTextureScale` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTextureScale` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetVector` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetVector` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetVectorArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetVectorArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetVectorArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetVectorArray` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### SoftJointLimit
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `bounciness` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `contactDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `limit` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Camera
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `activeTexture` | `RenderTexture (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `actualRenderingPath` | `RenderingPath (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `allowDynamicResolution` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `allowHDR` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `allowMSAA` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `areVRStereoViewMatricesWithinSingleCullTolerance` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `aspect` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `backgroundColor` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cameraToWorldMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cameraType` | `CameraType (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `clearFlags` | `CameraClearFlags (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `clearStencilAfterLightingPass` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `commandBufferCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cullingMask` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cullingMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `depth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `depthTextureMode` | `DepthTextureMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `eventMask` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `farClipPlane` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fieldOfView` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `focalLength` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forceIntoRenderTexture` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `layerCullDistances` | `float[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `layerCullSpherical` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lensShift` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `nearClipPlane` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `nonJitteredProjectionMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `opaqueSortMode` | `OpaqueSortMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `orthographic` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `orthographicSize` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `overrideSceneCullingMask` | `ulong` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pixelHeight` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pixelRect` | `Rect` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pixelWidth` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `previousViewProjectionMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `projectionMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rect` | `Rect` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderingPath` | `RenderingPath (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `scaledPixelHeight` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `scaledPixelWidth` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sensorSize` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stereoConvergence` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stereoEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stereoSeparation` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stereoTargetEye` | `StereoTargetEyeMask (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetDisplay` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetTexture` | `RenderTexture (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transparencySortAxis` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transparencySortMode` | `TransparencySortMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useJitteredProjectionMatrixForTransparentRendering` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useOcclusionCulling` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `usePhysicalProperties` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `velocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `worldToCameraMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AddCommandBuffer` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `AddCommandBufferAsync` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `CalculateFrustumCorners` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CalculateObliqueMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CopyFrom` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CopyStereoDeviceProjectionMatrixToNonJittered` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetCommandBuffers` | `CommandBuffer[] (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetGateFittedFieldOfView` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetGateFittedLensShift` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetStereoNonJitteredProjectionMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetStereoProjectionMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetStereoViewMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemoveAllCommandBuffers` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `RemoveCommandBuffer` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `RemoveCommandBuffers` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `Render` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RenderDontRestore` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RenderToCubemap` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RenderToCubemap` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RenderToCubemap` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RenderToCubemap` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RenderToCubemap` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RenderWithShader` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Reset` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `ResetAspect` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `ResetCullingMatrix` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `ResetProjectionMatrix` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `ResetReplacementShader` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `ResetStereoProjectionMatrices` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `ResetStereoViewMatrices` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `ResetTransparencySortSettings` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `ResetWorldToCameraMatrix` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `ScreenPointToRay` | `Ray (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ScreenPointToRay` | `Ray (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ScreenToViewportPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ScreenToWorldPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ScreenToWorldPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetReplacementShader` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `SetStereoProjectionMatrix` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `SetStereoViewMatrix` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `SetTargetBuffers` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `SetTargetBuffers` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `TryGetCullingParameters` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TryGetCullingParameters` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ViewportPointToRay` | `Ray (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ViewportPointToRay` | `Ray (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ViewportToScreenPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ViewportToWorldPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ViewportToWorldPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WorldToScreenPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WorldToScreenPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WorldToViewportPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WorldToViewportPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AnchoredJoint2D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `anchor` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `autoConfigureConnectedAnchor` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `connectedAnchor` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedRigidbody` | `Rigidbody2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `breakForce` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `breakTorque` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `connectedBody` | `Rigidbody2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableCollision` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reactionForce` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reactionTorque` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetReactionForce` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetReactionTorque` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CircleCollider2D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `radius` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedRigidbody` | `Rigidbody2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounciness` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `composite` | `CompositeCollider2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `density` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `errorState` | `ColliderErrorState2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `friction` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `offset` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shapeCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `PhysicsMaterial2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `usedByComposite` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `usedByEffector` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClosestPoint` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Distance` | `ColliderDistance2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShapeHash` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShapes` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShapes` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouching` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouching` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouching` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouchingLayers` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouchingLayers` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OverlapCollider` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OverlapCollider` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OverlapPoint` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemTrails
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `capacity` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AudioListener
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `velocityUpdateMode` | `AudioVelocityUpdateMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Compass
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `headingAccuracy` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `magneticHeading` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rawVector` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `timestamp` | `double` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `trueHeading` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### LayerMask
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `value` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Physics
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### TextMesh
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `alignment` | `TextAlignment (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `anchor` | `TextAnchor (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `characterSize` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `color` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `font` | `Font (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontSize` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontStyle` | `FontStyle (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lineSpacing` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `offsetZ` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `richText` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tabSize` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `text` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemShapeModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `alignToDirection` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `angle` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `arc` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `arcMode` | `ParticleSystemShapeMultiModeValue (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `arcSpeedMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `arcSpread` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `boxThickness` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `donutRadius` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `length` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mesh` | `Mesh (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `meshMaterialIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `meshRenderer` | `MeshRenderer` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `meshShapeType` | `ParticleSystemMeshShapeType (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `meshSpawnMode` | `ParticleSystemShapeMultiModeValue (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `meshSpawnSpeedMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `meshSpawnSpread` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `normalOffset` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `position` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `radius` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `radiusMode` | `ParticleSystemShapeMultiModeValue (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `radiusSpeedMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `radiusSpread` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `radiusThickness` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `randomDirectionAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `randomPositionAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rotation` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `scale` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shapeType` | `ParticleSystemShapeType (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `skinnedMeshRenderer` | `SkinnedMeshRenderer` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sphericalDirectionAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sprite` | `Sprite (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spriteRenderer` | `SpriteRenderer (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `texture` | `Texture2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textureAlphaAffectsParticles` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textureBilinearFiltering` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textureClipChannel` | `ParticleSystemShapeTextureChannel (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textureClipThreshold` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textureColorAffectsParticles` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textureUVChannel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useMeshColors` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useMeshMaterialIndex` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Canvas
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `additionalShaderChannels` | `AdditionalCanvasShaderChannels (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cachedSortingLayerValue` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isRootCanvas` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `normalizedSortingGridSize` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `overridePixelPerfect` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `overrideSorting` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pixelPerfect` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pixelRect` | `Rect` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `planeDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `referencePixelsPerUnit` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderingDisplaySize` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderMode` | `RenderMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderOrder` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rootCanvas` | `Canvas` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `scaleFactor` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingLayerID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingLayerName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingOrder` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetDisplay` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `worldCamera` | `Camera` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### WheelHit
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `collider` | `Collider` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `force` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forwardDir` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forwardSlip` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `normal` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `point` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sidewaysDir` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sidewaysSlip` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Transform
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `_parent_impl` | `Transform` | `ANY` | `ANY` | `ANY` | `ANY` |
| `childCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `eulerAngles` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forward` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasChanged` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hierarchyCapacity` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hierarchyCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localEulerAngles` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localRotation` | `Quaternion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localScale` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localToWorldMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lossyScale` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `parent` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `position` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `right` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rotation` | `Quaternion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `up` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `worldToLocalMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Find` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetChild` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetEnumerator` | `IEnumerator (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetLocalPositionAndRotation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPositionAndRotation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetSiblingIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `InverseTransformDirection` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `InverseTransformDirection` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `InverseTransformPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `InverseTransformPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `InverseTransformVector` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `InverseTransformVector` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsChildOf` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LookAt` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `LookAt` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `LookAt` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `LookAt` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `Rotate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `Rotate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `Rotate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `Rotate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `Rotate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `Rotate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `RotateAround` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `SetAsFirstSibling` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `SetAsLastSibling` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `SetLocalPositionAndRotation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `SetPositionAndRotation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `SetSiblingIndex` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `TransformDirection` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TransformDirection` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TransformPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TransformPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TransformVector` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TransformVector` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Translate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `Translate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `Translate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `Translate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `Translate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `Translate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Gradient
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `alphaKeys` | `GradientAlphaKey[] (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colorKeys` | `GradientColorKey[] (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mode` | `GradientMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Evaluate` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetKeys` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Collider
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `attachedArticulationBody` | `ArticulationBody (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedRigidbody` | `Rigidbody` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `contactOffset` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasModifiableContacts` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material` | `PhysicMaterial (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `PhysicMaterial (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ClosestPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClosestPointOnBounds` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### StateMachineBehaviour
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `OnStateEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateIK` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateIK` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMachineEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMachineEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMachineExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMachineExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMove` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateMove` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateUpdate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnStateUpdate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### BoxCollider
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `center` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `size` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedArticulationBody` | `ArticulationBody (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedRigidbody` | `Rigidbody` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `contactOffset` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasModifiableContacts` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material` | `PhysicMaterial (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `PhysicMaterial (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ClosestPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClosestPointOnBounds` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CapsuleCollider
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `center` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `direction` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `height` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `radius` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedArticulationBody` | `ArticulationBody (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedRigidbody` | `Rigidbody` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `contactOffset` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasModifiableContacts` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material` | `PhysicMaterial (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `PhysicMaterial (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ClosestPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClosestPointOnBounds` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Collision
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `articulationBody` | `ArticulationBody (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `body` | `Component` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `collider` | `Collider` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `contactCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `contacts` | `ReadOnlyCollection<ContactPoint> (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `impulse` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `relativeVelocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rigidbody` | `Rigidbody` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetContact` | `ContactPoint (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CanvasGroup
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `alpha` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `blocksRaycasts` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ignoreParentGroups` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `interactable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `IsRaycastLocationValid` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CapsuleCollider2D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `direction` | `CapsuleDirection2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `size` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedRigidbody` | `Rigidbody2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounciness` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `composite` | `CompositeCollider2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `density` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `errorState` | `ColliderErrorState2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `friction` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `offset` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shapeCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `PhysicsMaterial2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `usedByComposite` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `usedByEffector` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClosestPoint` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Distance` | `ColliderDistance2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShapeHash` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShapes` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShapes` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouching` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouching` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouching` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouchingLayers` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouchingLayers` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OverlapCollider` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OverlapCollider` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OverlapPoint` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Behaviour
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### MonoBehaviour
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemInheritVelocityModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `curveMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mode` | `ParticleSystemInheritVelocityMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemEmitParams
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `angularVelocity` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `angularVelocity3D` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `applyShapeToPosition` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `axisOfRotation` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `particle` | `ParticleSystemParticle` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `position` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `randomSeed` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rotation` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rotation3D` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `startColor` | `Color32` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `startLifetime` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `startSize` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `startSize3D` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `velocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetAngularVelocity` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetAxisOfRotation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetMeshIndex` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetPosition` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetRandomSeed` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetRotation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetStartColor` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetStartLifetime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetStartSize` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetVelocity` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### BaseInstanceWrapper<GameObject>
### GameObject
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `activeInHierarchy` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `activeSelf` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isStatic` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `layer` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sceneCullingMask` | `ulong` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetComponent` | `DynValue (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetComponentInChildren` | `DynValue (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetComponentInParent` | `DynValue (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetComponents` | `Component[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetComponents` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetComponentsInChildren` | `Component[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetComponentsInChildren` | `Component[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetComponentsInParent` | `Component[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetComponentsInParent` | `Component[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetActive` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `SELF` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemRotationBySpeedModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `range` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `separateAxes` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `xMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `yMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `zMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Quaternion
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `eulerAngles` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `normalized` | `Quaternion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `w` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `x` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Normalize` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Set` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetFromToRotation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLookRotation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLookRotation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToAngleAxis` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AudioSettings
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ScriptableObject
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### SoftJointLimitSpring
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `damper` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spring` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemLimitVelocityOverLifetimeModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `dampen` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `dragMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `limitMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `limitXMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `limitYMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `limitZMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `multiplyDragByParticleSize` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `multiplyDragByParticleVelocity` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `separateAxes` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `space` | `ParticleSystemSimulationSpace (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Animator
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `angularVelocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `applyRootMotion` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `avatar` | `Avatar` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bodyPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bodyRotation` | `Quaternion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cullingMode` | `AnimatorCullingMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `deltaPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `deltaRotation` | `Quaternion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `feetPivotActive` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fireEvents` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gravityWeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasBoundPlayables` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasRootMotion` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasTransformHierarchy` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `humanScale` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isHuman` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isInitialized` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isMatchingTarget` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isOptimizable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `keepAnimatorStateOnDisable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `layerCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `layersAffectMassCenter` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `leftFeetBottomHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `logWarnings` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `parameterCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `parameters` | `ReadOnlyCollection<AnimatorControllerParameter>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pivotPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pivotWeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playableGraph` | `PlayableGraph (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playbackTime` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `recorderMode` | `AnimatorRecorderMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `recorderStartTime` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `recorderStopTime` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rightFeetBottomHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rootPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rootRotation` | `Quaternion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `runtimeAnimatorController` | `RuntimeAnimatorController` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `speed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stabilizeFeet` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetRotation` | `Quaternion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `updateMode` | `AnimatorUpdateMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `velocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `writeDefaultValuesOnDisable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ApplyBuiltinRootMotion` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFade` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFade` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFade` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFade` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFade` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFade` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFade` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFade` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeInFixedTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeInFixedTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeInFixedTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeInFixedTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeInFixedTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeInFixedTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeInFixedTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeInFixedTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetAnimatorTransitionInfo` | `AnimatorTransitionInfo (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetBehaviours` | `StateMachineBehaviour[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetBoneTransform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetBool` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetBool` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetCurrentAnimatorClipInfo` | `AnimatorClipInfo[] (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetCurrentAnimatorClipInfo` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetCurrentAnimatorClipInfoCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetCurrentAnimatorStateInfo` | `AnimatorStateInfo (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetFloat` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetFloat` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetIKHintPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetIKHintPositionWeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetIKPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetIKPositionWeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetIKRotation` | `Quaternion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetIKRotationWeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInteger` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInteger` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetLayerIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetLayerName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetLayerWeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetNextAnimatorClipInfo` | `AnimatorClipInfo[] (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetNextAnimatorClipInfo` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetNextAnimatorClipInfoCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetNextAnimatorStateInfo` | `AnimatorStateInfo (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetParameter` | `AnimatorControllerParameter` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasState` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `InterruptMatchTarget` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `InterruptMatchTarget` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsInTransition` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsParameterControlledByCurve` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsParameterControlledByCurve` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MatchTarget` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MatchTarget` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MatchTarget` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Play` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Play` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Play` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Play` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Play` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Play` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlayInFixedTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlayInFixedTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlayInFixedTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlayInFixedTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlayInFixedTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlayInFixedTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Rebind` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetBoneLocalRotation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetBool` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetBool` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetFloat` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetFloat` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetFloat` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetFloat` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetIKHintPosition` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetIKHintPositionWeight` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetIKPosition` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetIKPositionWeight` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetIKRotation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetIKRotationWeight` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetInteger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetInteger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLayerWeight` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLookAtPosition` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLookAtWeight` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLookAtWeight` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLookAtWeight` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLookAtWeight` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLookAtWeight` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTarget` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTrigger` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `StartPlayback` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `StartRecording` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `StopPlayback` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `StopRecording` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Update` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WriteDefaultValues` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### RuntimeAnimatorController
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `animationClips` | `ReadOnlyCollection<AnimationClip>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AudioSource
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `bypassEffects` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bypassListenerEffects` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bypassReverbZones` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `clip` | `AudioClip` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `dopplerLevel` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ignoreListenerPause` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ignoreListenerVolume` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isPlaying` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isVirtual` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `loop` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mute` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `outputAudioMixerGroup` | `AudioMixerGroup (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `panStereo` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pitch` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playOnAwake` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `priority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reverbZoneMix` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rolloffMode` | `AudioRolloffMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spatialBlend` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spatialize` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spatializePostEffects` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spread` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `time` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `timeSamples` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `velocityUpdateMode` | `AudioVelocityUpdateMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `volume` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetAmbisonicDecoderFloat` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetCustomCurve` | `AnimationCurve` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetOutputData` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetSpatializerFloat` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetSpectrumData` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Pause` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Play` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Play` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlayDelayed` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlayOneShot` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlayOneShot` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlayScheduled` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetAmbisonicDecoderFloat` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetCustomCurve` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetScheduledEndTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetScheduledStartTime` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetSpatializerFloat` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Stop` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UnPause` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Cloth
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `bendingStiffness` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `capsuleColliders` | `CapsuleCollider[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `clothSolverFrequency` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `coefficients` | `ClothSkinningCoefficient[] (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `collisionMassScale` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `damping` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableContinuousCollision` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `externalAcceleration` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `friction` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `normals` | `ReadOnlyCollection<Vector3>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `randomAcceleration` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `selfCollisionDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `selfCollisionStiffness` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sleepThreshold` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sphereColliders` | `ClothSphereColliderPair[] (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stiffnessFrequency` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stretchingStiffness` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useGravity` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useTethers` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useVirtualParticles` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `vertices` | `ReadOnlyCollection<Vector3>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `worldAccelerationScale` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `worldVelocityScale` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ClearTransformMotion` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetSelfAndInterCollisionIndices` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetVirtualParticleIndices` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetVirtualParticleWeights` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetEnabledFading` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetEnabledFading` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetSelfAndInterCollisionIndices` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetVirtualParticleIndices` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetVirtualParticleWeights` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### RaycastHit2D
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `centroid` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `collider` | `Collider2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `distance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fraction` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `normal` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `point` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rigidbody` | `Rigidbody2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTo` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Texture
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `anisoLevel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `dimension` | `TextureDimension (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `filterMode` | `FilterMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `graphicsFormat` | `GraphicsFormat (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `height` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isReadable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mipMapBias` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mipmapCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `texelSize` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `updateCount` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `width` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapMode` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapModeU` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapModeV` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapModeW` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetNativeTexturePtr` | `IntPtr (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IncrementUpdateCount` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ConfigurableJoint
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `angularXDrive` | `JointDrive` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `angularXLimitSpring` | `SoftJointLimitSpring` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `angularXMotion` | `ConfigurableJointMotion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `angularYLimit` | `SoftJointLimit` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `angularYMotion` | `ConfigurableJointMotion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `angularYZDrive` | `JointDrive` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `angularYZLimitSpring` | `SoftJointLimitSpring` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `angularZLimit` | `SoftJointLimit` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `angularZMotion` | `ConfigurableJointMotion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `configuredInWorldSpace` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `highAngularXLimit` | `SoftJointLimit` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `linearLimit` | `SoftJointLimit` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `linearLimitSpring` | `SoftJointLimitSpring` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lowAngularXLimit` | `SoftJointLimit` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `projectionAngle` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `projectionDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `projectionMode` | `JointProjectionMode` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rotationDriveMode` | `RotationDriveMode` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `secondaryAxis` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `slerpDrive` | `JointDrive` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `swapBodies` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetAngularVelocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetRotation` | `Quaternion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetVelocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `xDrive` | `JointDrive` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `xMotion` | `ConfigurableJointMotion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `yDrive` | `JointDrive` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `yMotion` | `ConfigurableJointMotion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `zDrive` | `JointDrive` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `zMotion` | `ConfigurableJointMotion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `anchor` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `autoConfigureConnectedAnchor` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `axis` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `breakForce` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `breakTorque` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `connectedAnchor` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `connectedArticulationBody` | `ArticulationBody (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `connectedBody` | `Rigidbody` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `connectedMassScale` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentForce` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentTorque` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableCollision` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enablePreprocessing` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `massScale` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Joint2D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `attachedRigidbody` | `Rigidbody2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `breakForce` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `breakTorque` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `connectedBody` | `Rigidbody2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableCollision` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reactionForce` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reactionTorque` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetReactionForce` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetReactionTorque` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemSizeBySpeedModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `range` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `separateAxes` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sizeMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `xMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `yMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `zMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Cubemap
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `desiredMipmapLevel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `format` | `TextureFormat (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isReadable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `loadedMipmapLevel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `loadingMipmapLevel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `requestedMipmapLevel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `streamingMipmaps` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `streamingMipmapsPriority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `anisoLevel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `dimension` | `TextureDimension (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `filterMode` | `FilterMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `graphicsFormat` | `GraphicsFormat (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `height` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mipMapBias` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mipmapCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `texelSize` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `updateCount` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `width` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapMode` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapModeU` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapModeV` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapModeW` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Apply` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Apply` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Apply` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClearRequestedMipmapLevel` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixel` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixel` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels` | `Color[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels` | `Color[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsRequestedMipmapLevelLoaded` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixel` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixel` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SmoothEdges` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SmoothEdges` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateExternalTexture` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetNativeTexturePtr` | `IntPtr (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IncrementUpdateCount` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemMainModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `subEmittersCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddSubEmitter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddSubEmitter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetSubEmitterEmitProbability` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetSubEmitterProperties` | `ParticleSystemSubEmitterProperties (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetSubEmitterSystem` | `ParticleSystem` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetSubEmitterType` | `ParticleSystemSubEmitterType (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemoveSubEmitter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemoveSubEmitter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetSubEmitterEmitProbability` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetSubEmitterProperties` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetSubEmitterSystem` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetSubEmitterType` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemVelocityOverLifetimeModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `orbitalOffsetXMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `orbitalOffsetYMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `orbitalOffsetZMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `orbitalXMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `orbitalYMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `orbitalZMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `radialMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `space` | `ParticleSystemSimulationSpace (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `speedModifierMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `xMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `yMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `zMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemCollisionModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `bounceMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colliderForce` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `collidesWith` | `LayerMask` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `dampenMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableDynamicColliders` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lifetimeLossMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxCollisionShapes` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxKillSpeed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minKillSpeed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mode` | `ParticleSystemCollisionMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `multiplyColliderForceByCollisionAngle` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `multiplyColliderForceByParticleSize` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `multiplyColliderForceByParticleSpeed` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `planeCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `quality` | `ParticleSystemCollisionQuality (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `radiusScale` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sendCollisionMessages` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `type` | `ParticleSystemCollisionType (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `voxelSize` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddPlane` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPlane` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemovePlane` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemovePlane` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPlane` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### BoxCollider2D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `autoTiling` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `edgeRadius` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `size` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedRigidbody` | `Rigidbody2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounciness` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `composite` | `CompositeCollider2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `density` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `errorState` | `ColliderErrorState2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `friction` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `offset` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shapeCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `PhysicsMaterial2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `usedByComposite` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `usedByEffector` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClosestPoint` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Distance` | `ColliderDistance2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShapeHash` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShapes` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShapes` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouching` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouching` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouching` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouchingLayers` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouchingLayers` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OverlapCollider` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OverlapCollider` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OverlapPoint` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemBurst
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `cycleCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxCount` | `short` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minCount` | `short` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `probability` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `repeatInterval` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `time` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AudioReverbZone
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `decayHFRatio` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `decayTime` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `density` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `diffusion` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HFReference` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LFReference` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reflections` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reflectionsDelay` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reverb` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reverbDelay` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reverbPreset` | `AudioReverbPreset` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `room` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `roomHF` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `roomLF` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Renderer
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `allowOcclusionWhenDynamic` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forceRenderingOff` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isPartOfStaticBatch` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isVisible` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightmapIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightmapScaleOffset` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightProbeProxyVolumeOverride` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightProbeUsage` | `LightProbeUsage (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localBounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localToWorldMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `materials` | `Material[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `motionVectorGenerationMode` | `MotionVectorGenerationMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `probeAnchor` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rayTracingMode` | `RayTracingMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `realtimeLightmapIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `realtimeLightmapScaleOffset` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `receiveShadows` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reflectionProbeUsage` | `ReflectionProbeUsage (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rendererPriority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderingLayerMask` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shadowCastingMode` | `ShadowCastingMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterials` | `Material[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingLayerID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingLayerName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingOrder` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `staticShadowCaster` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `worldToLocalMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetClosestReflectionProbes` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetMaterials` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetSharedMaterials` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasPropertyBlock` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetBounds` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetLocalBounds` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ColorUtility
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AvatarMask
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `transformCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AddTransformPath` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddTransformPath` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetHumanoidBodyPartActive` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTransformActive` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTransformPath` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemoveTransformPath` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemoveTransformPath` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetHumanoidBodyPartActive` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTransformActive` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTransformPath` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Vector2
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `magnitude` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `normalized` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sqrMagnitude` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `x` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Normalize` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Scale` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Set` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SqrMagnitude` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemMinMaxGradient
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `color` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colorMax` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colorMin` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gradient` | `Gradient` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gradientMax` | `Gradient` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gradientMin` | `Gradient` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mode` | `ParticleSystemGradientMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Evaluate` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Evaluate` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### TerrainCollider
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `terrainData` | `TerrainData (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedArticulationBody` | `ArticulationBody (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedRigidbody` | `Rigidbody` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `contactOffset` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasModifiableContacts` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material` | `PhysicMaterial (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `PhysicMaterial (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ClosestPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClosestPointOnBounds` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AudioClip
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ambisonic` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `channels` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `frequency` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `length` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `loadInBackground` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `loadState` | `AudioDataLoadState (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `loadType` | `AudioClipLoadType (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preloadAudioData` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `samples` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetData` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Rigidbody
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `angularDrag` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `angularVelocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `centerOfMass` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `collisionDetectionMode` | `CollisionDetectionMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `constraints` | `RigidbodyConstraints (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `detectCollisions` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `drag` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `freezeRotation` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `inertiaTensor` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `inertiaTensorRotation` | `Quaternion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `interpolation` | `RigidbodyInterpolation (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isKinematic` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mass` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxAngularVelocity` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxDepenetrationVelocity` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `position` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rotation` | `Quaternion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sleepThreshold` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `solverIterations` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `solverVelocityIterations` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useGravity` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `velocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `worldCenterOfMass` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AddExplosionForce` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddExplosionForce` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddExplosionForce` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddForce` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddForce` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddForce` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddForce` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddForceAtPosition` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddForceAtPosition` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddRelativeForce` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddRelativeForce` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddRelativeForce` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddRelativeForce` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddRelativeTorque` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddRelativeTorque` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddRelativeTorque` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddRelativeTorque` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddTorque` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddTorque` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddTorque` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddTorque` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClosestPointOnBounds` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPointVelocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetRelativePointVelocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsSleeping` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MovePosition` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MoveRotation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetCenterOfMass` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetInertiaTensor` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetDensity` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Sleep` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SweepTest` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SweepTest` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SweepTest` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SweepTestAll` | `RaycastHit[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SweepTestAll` | `RaycastHit[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SweepTestAll` | `RaycastHit[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `WakeUp` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### JointDrive
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `maximumForce` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `positionDamper` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `positionSpring` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ScriptableCullingParameters
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `accurateOcclusionThreshold` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cameraProperties` | `CameraProperties (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `conservativeEnclosingSphere` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cullingMask` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cullingMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cullingOptions` | `CullingOptions (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cullingPlaneCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isOrthographic` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lodParameters` | `LODParameters (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maximumPortalCullingJobs` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maximumVisibleLights` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `numIterationsEnclosingSphere` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `origin` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reflectionProbeSortingCriteria` | `ReflectionProbeSortingCriteria (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shadowDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shadowNearPlaneOffset` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stereoProjectionMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stereoSeparationDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stereoViewMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetCullingPlane` | `Plane (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetLayerCullingDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetCullingPlane` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLayerCullingDistance` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### PhysicsMaterial2D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `bounciness` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `friction` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemExternalForcesModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `influenceCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `influenceFilter` | `ParticleSystemGameObjectFilter (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `influenceMask` | `LayerMask` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `multiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddInfluence` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInfluence` | `ParticleSystemForceField (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsAffectedBy` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemoveAllInfluences` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemoveInfluence` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemoveInfluence` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetInfluence` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemEmissionModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `burstCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rateOverDistanceMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rateOverTimeMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetBurst` | `ParticleSystemBurst` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetBursts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetBurst` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetBursts` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetBursts` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### PhysicsUpdateBehaviour2D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Color32
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `a` | `byte` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `b` | `byte` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `g` | `byte` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `r` | `byte` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### BoundingSphere
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `position` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `radius` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CubemapArray
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `cubemapCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `format` | `TextureFormat (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isReadable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `anisoLevel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `dimension` | `TextureDimension (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `filterMode` | `FilterMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `graphicsFormat` | `GraphicsFormat (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `height` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mipMapBias` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mipmapCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `texelSize` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `updateCount` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `width` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapMode` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapModeU` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapModeV` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapModeW` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Apply` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Apply` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Apply` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels` | `Color[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels` | `Color[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels32` | `Color32[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels32` | `Color32[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels32` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels32` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetNativeTexturePtr` | `IntPtr (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IncrementUpdateCount` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Effector2D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `colliderMask` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useColliderMask` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Collider2D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `attachedRigidbody` | `Rigidbody2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounciness` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `composite` | `CompositeCollider2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `density` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `errorState` | `ColliderErrorState2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `friction` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `offset` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shapeCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `PhysicsMaterial2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `usedByComposite` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `usedByEffector` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClosestPoint` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Distance` | `ColliderDistance2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShapeHash` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShapes` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShapes` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouching` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouching` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouching` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouchingLayers` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouchingLayers` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OverlapCollider` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OverlapCollider` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OverlapPoint` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemColorOverLifetimeModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `color` | `ParticleSystemMinMaxGradient` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### BillboardRenderer
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `billboard` | `BillboardAsset` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `allowOcclusionWhenDynamic` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forceRenderingOff` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isPartOfStaticBatch` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isVisible` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightmapIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightmapScaleOffset` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightProbeProxyVolumeOverride` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightProbeUsage` | `LightProbeUsage (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localBounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localToWorldMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `materials` | `Material[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `motionVectorGenerationMode` | `MotionVectorGenerationMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `probeAnchor` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rayTracingMode` | `RayTracingMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `realtimeLightmapIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `realtimeLightmapScaleOffset` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `receiveShadows` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reflectionProbeUsage` | `ReflectionProbeUsage (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rendererPriority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderingLayerMask` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shadowCastingMode` | `ShadowCastingMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterials` | `Material[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingLayerID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingLayerName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingOrder` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `staticShadowCaster` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `worldToLocalMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetClosestReflectionProbes` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetMaterials` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetSharedMaterials` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasPropertyBlock` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetBounds` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetLocalBounds` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AnimationClip
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `empty` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `events` | `AnimationEvent[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `frameRate` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasGenericRootTransform` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasMotionCurves` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasMotionFloatCurves` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasRootCurves` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `humanMotion` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `legacy` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `length` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localBounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapMode` | `WrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `apparentSpeed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `averageAngularSpeed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `averageDuration` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `averageSpeed` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isHumanMotion` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isLooping` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AddEvent` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClearCurves` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `EnsureQuaternionContinuity` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SampleAnimation` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetCurve` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemForceOverLifetimeModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `randomized` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `space` | `ParticleSystemSimulationSpace (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `xMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `yMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `zMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Matrix4x4
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `decomposeProjection` | `FrustumPlanes (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `determinant` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `inverse` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isIdentity` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lossyScale` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m00` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m01` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m02` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m03` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m10` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m11` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m12` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m13` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m20` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m21` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m22` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m23` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m30` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m31` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m32` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `m33` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rotation` | `Quaternion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transpose` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetColumn` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetRow` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MultiplyPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MultiplyPoint3x4` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MultiplyVector` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetColumn` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetRow` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTRS` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TransformPlane` | `Plane (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ValidTRS` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AnimationCurve
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `keys` | `ReadOnlyCollection<Keyframe> (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `length` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `postWrapMode` | `WrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preWrapMode` | `WrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AddKey` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddKey` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Evaluate` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MoveKey` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemoveKey` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SmoothTangents` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemRotationOverLifetimeModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `separateAxes` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `xMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `yMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `zMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemTrailModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `attachRibbonsToTransform` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colorOverLifetime` | `ParticleSystemMinMaxGradient` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colorOverTrail` | `ParticleSystemMinMaxGradient` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `dieWithParticles` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `generateLightingData` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `inheritParticleColor` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lifetimeMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minVertexDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mode` | `ParticleSystemTrailMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ratio` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ribbonCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shadowBias` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sizeAffectsLifetime` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sizeAffectsWidth` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `splitSubEmitterRibbons` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textureMode` | `ParticleSystemTrailTextureMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `widthOverTrailMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `worldSpace` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### TrackedReference
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AnimatorUtility
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CharacterJoint
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enableProjection` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `highTwistLimit` | `SoftJointLimit` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lowTwistLimit` | `SoftJointLimit` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `projectionAngle` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `projectionDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `swing1Limit` | `SoftJointLimit` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `swing2Limit` | `SoftJointLimit` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `swingAxis` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `swingLimitSpring` | `SoftJointLimitSpring` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `twistLimitSpring` | `SoftJointLimitSpring` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `anchor` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `autoConfigureConnectedAnchor` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `axis` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `breakForce` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `breakTorque` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `connectedAnchor` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `connectedArticulationBody` | `ArticulationBody (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `connectedBody` | `Rigidbody` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `connectedMassScale` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentForce` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentTorque` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableCollision` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enablePreprocessing` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `massScale` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### MeshCollider
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `convex` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cookingOptions` | `MeshColliderCookingOptions (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMesh` | `Mesh (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedArticulationBody` | `ArticulationBody (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedRigidbody` | `Rigidbody` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `contactOffset` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasModifiableContacts` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material` | `PhysicMaterial (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `PhysicMaterial (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ClosestPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClosestPointOnBounds` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Joint
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `anchor` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `autoConfigureConnectedAnchor` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `axis` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `breakForce` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `breakTorque` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `connectedAnchor` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `connectedArticulationBody` | `ArticulationBody (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `connectedBody` | `Rigidbody` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `connectedMassScale` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentForce` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentTorque` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enableCollision` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enablePreprocessing` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `massScale` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AnimatorOverrideController
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `overridesCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `runtimeAnimatorController` | `RuntimeAnimatorController` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animationClips` | `ReadOnlyCollection<AnimationClip>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ApplyOverrides` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetOverrides` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Scene
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `buildIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `handle` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isDirty` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isLoaded` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isSubScene` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `path` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rootCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsValid` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ConstantForce2D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `force` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `relativeForce` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `torque` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### BaseInstanceWrapper<Transform>
### Collision2D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `collider` | `Collider2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `contactCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `contacts` | `ReadOnlyCollection<ContactPoint2D> (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `otherCollider` | `Collider2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `otherRigidbody` | `Rigidbody2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `relativeVelocity` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rigidbody` | `Rigidbody2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetContact` | `ContactPoint2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AnimationEvent
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `animationState` | `AnimationState` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorClipInfo` | `AnimatorClipInfo (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animatorStateInfo` | `AnimatorStateInfo (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `floatParameter` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `functionName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `intParameter` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isFiredByAnimator` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isFiredByLegacy` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `messageOptions` | `SendMessageOptions (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `objectReferenceParameter` | `UnityObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stringParameter` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `time` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Color
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `a` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `b` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `g` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gamma` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `grayscale` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `linear` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxColorComponent` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `r` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemTextureSheetAnimationModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `animation` | `ParticleSystemAnimationType (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cycleCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fps` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `frameOverTimeMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mode` | `ParticleSystemAnimationMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `numTilesX` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `numTilesY` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rowIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rowMode` | `ParticleSystemAnimationRowMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `speedRange` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spriteCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `startFrameMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `timeMode` | `ParticleSystemAnimationTimeMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `uvChannelMask` | `UVChannelFlags (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddSprite` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetSprite` | `Sprite (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemoveSprite` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetSprite` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### UnityObject
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### WheelCollider
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `brakeTorque` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `center` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forceAppPointDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forwardFriction` | `WheelFrictionCurve (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isGrounded` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mass` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `motorTorque` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `radius` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rpm` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sidewaysFriction` | `WheelFrictionCurve (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sprungMass` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `steerAngle` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `suspensionDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `suspensionExpansionLimited` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `suspensionSpring` | `JointSpring (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wheelDampingRate` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedArticulationBody` | `ArticulationBody (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedRigidbody` | `Rigidbody` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `contactOffset` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasModifiableContacts` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material` | `PhysicMaterial (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `PhysicMaterial (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ConfigureVehicleSubsteps` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetGroundHit` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetWorldPose` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetSprungMasses` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClosestPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClosestPointOnBounds` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### BuoyancyEffector2D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `angularDrag` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `density` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flowAngle` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flowMagnitude` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flowVariation` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `linearDrag` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `surfaceLevel` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colliderMask` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useColliderMask` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemNoiseModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `damping` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `frequency` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `octaveCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `octaveMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `octaveScale` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `quality` | `ParticleSystemNoiseQuality (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `remapEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `remapMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `remapXMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `remapYMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `remapZMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `scrollSpeedMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `separateAxes` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `strengthMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `strengthXMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `strengthYMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `strengthZMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Vector3Int
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `magnitude` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sqrMagnitude` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `x` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `y` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `z` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Clamp` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Scale` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Set` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CanvasRenderer
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `absoluteDepth` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `clippingSoftness` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cull` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cullTransparentMesh` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasMoved` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasPopInstruction` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasRectClipping` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `materialCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `popMaterialCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `relativeDepth` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Clear` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DisableRectClipping` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `EnableRectClipping` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetAlpha` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetColor` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInheritedAlpha` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetMaterial` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetMaterial` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPopMaterial` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetAlpha` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetAlphaTexture` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetColor` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetMaterial` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetMaterial` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetMesh` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPopMaterial` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTexture` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Mathf
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AudioRenderer
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `CLIENT` | `AVATAR` | `LOCAL` | `ANY` |
### Vector4
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `magnitude` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `normalized` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sqrMagnitude` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `w` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `x` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Normalize` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Scale` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Set` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SqrMagnitude` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### SkinnedMeshRenderer
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `bones` | `Transform[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `quality` | `SkinQuality (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rootBone` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMesh` | `Mesh (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `skinnedMotionVectors` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `updateWhenOffscreen` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `allowOcclusionWhenDynamic` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forceRenderingOff` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isPartOfStaticBatch` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isVisible` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightmapIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightmapScaleOffset` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightProbeProxyVolumeOverride` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightProbeUsage` | `LightProbeUsage (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localBounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localToWorldMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `materials` | `Material[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `motionVectorGenerationMode` | `MotionVectorGenerationMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `probeAnchor` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rayTracingMode` | `RayTracingMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `realtimeLightmapIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `realtimeLightmapScaleOffset` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `receiveShadows` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reflectionProbeUsage` | `ReflectionProbeUsage (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rendererPriority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderingLayerMask` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shadowCastingMode` | `ShadowCastingMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterials` | `Material[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingLayerID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingLayerName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingOrder` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `staticShadowCaster` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `worldToLocalMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetBlendShapeWeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPreviousVertexBuffer` | `GraphicsBuffer (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetVertexBuffer` | `GraphicsBuffer (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetBlendShapeWeight` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetClosestReflectionProbes` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetMaterials` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetSharedMaterials` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasPropertyBlock` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetBounds` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetLocalBounds` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### RaycastHit
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `articulationBody` | `ArticulationBody (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `barycentricCoordinate` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `collider` | `Collider` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colliderInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `distance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightmapCoord` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `normal` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `point` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rigidbody` | `Rigidbody` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textureCoord` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textureCoord2` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `triangleIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Texture3D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `depth` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `format` | `TextureFormat (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isReadable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `anisoLevel` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `dimension` | `TextureDimension (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `filterMode` | `FilterMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `graphicsFormat` | `GraphicsFormat (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `height` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mipMapBias` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mipmapCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `texelSize` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `updateCount` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `width` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapMode` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapModeU` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapModeV` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapModeW` | `TextureWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Apply` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Apply` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Apply` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixel` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixel` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixelBilinear` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixelBilinear` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels` | `Color[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels` | `Color[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels32` | `Color32[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPixels32` | `Color32[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixel` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixel` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels32` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPixels32` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UpdateExternalTexture` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetNativeTexturePtr` | `IntPtr (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IncrementUpdateCount` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### BillboardAsset
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `bottom` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `height` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `imageCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `indexCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `vertexCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `width` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetImageTexCoords` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetImageTexCoords` | `Vector4[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetIndices` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetIndices` | `ushort[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetVertices` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetVertices` | `Vector2[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetImageTexCoords` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetImageTexCoords` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetIndices` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetIndices` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetVertices` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetVertices` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AudioBehaviour
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemPlaybackState
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemCustomDataModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetColor` | `ParticleSystemMinMaxGradient` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetMode` | `ParticleSystemCustomDataMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetVectorComponentCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetColor` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetMode` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetVector` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetVectorComponentCount` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystem
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `collision` | `ParticleSystemCollisionModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colorBySpeed` | `ParticleSystemColorBySpeedModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colorOverLifetime` | `ParticleSystemColorOverLifetimeModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `customData` | `ParticleSystemCustomDataModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `emission` | `ParticleSystemEmissionModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `externalForces` | `ParticleSystemExternalForcesModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forceOverLifetime` | `ParticleSystemForceOverLifetimeModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `inheritVelocity` | `ParticleSystemInheritVelocityModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isEmitting` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isPaused` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isPlaying` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isStopped` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lifetimeByEmitterSpeed` | `ParticleSystemLifetimeByEmitterSpeedModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lights` | `ParticleSystemLightsModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `limitVelocityOverLifetime` | `ParticleSystemLimitVelocityOverLifetimeModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `noise` | `ParticleSystemNoiseModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `particleCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `proceduralSimulationSupported` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `randomSeed` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rotationBySpeed` | `ParticleSystemRotationBySpeedModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rotationOverLifetime` | `ParticleSystemRotationOverLifetimeModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shape` | `ParticleSystemShapeModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sizeBySpeed` | `ParticleSystemSizeBySpeedModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sizeOverLifetime` | `ParticleSystemSizeOverLifetimeModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `subEmitters` | `ParticleSystemMainModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textureSheetAnimation` | `ParticleSystemTextureSheetAnimationModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `time` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `trails` | `ParticleSystemTrailModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useAutoRandomSeed` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `velocityOverLifetime` | `ParticleSystemVelocityOverLifetimeModule` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AllocateAxisOfRotationAttribute` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AllocateMeshIndexAttribute` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Clear` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Clear` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Emit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPlaybackState` | `ParticleSystemPlaybackState` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetTrails` | `ParticleSystemTrails` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsAlive` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsAlive` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Pause` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Pause` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Play` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Play` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Simulate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Simulate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Simulate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Simulate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Stop` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Stop` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TriggerSubEmitter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemLifetimeByEmitterSpeedModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `curveMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `range` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ConstantForce
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `force` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `relativeForce` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `relativeTorque` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `torque` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Animation
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `animatePhysics` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `clip` | `AnimationClip` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cullingType` | `AnimationCullingType (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isPlaying` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localBounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `playAutomatically` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wrapMode` | `WrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AddClip` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddClip` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddClip` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Blend` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Blend` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Blend` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFade` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFade` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFade` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeQueued` | `AnimationState` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeQueued` | `AnimationState` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeQueued` | `AnimationState` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CrossFadeQueued` | `AnimationState` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetClip` | `AnimationClip` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetClipCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetEnumerator` | `IEnumerator (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsPlaying` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Play` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Play` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Play` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Play` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlayQueued` | `AnimationState` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlayQueued` | `AnimationState` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlayQueued` | `AnimationState` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemoveClip` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemoveClip` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Rewind` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Rewind` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Sample` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Stop` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Stop` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SyncLayer` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemSizeOverLifetimeModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `separateAxes` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sizeMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `xMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `yMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `zMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemLightsModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `alphaAffectsIntensity` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `intensityMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `light` | `Light (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxLights` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rangeMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ratio` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sizeAffectsRange` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useParticleColor` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useRandomDistribution` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AreaEffector2D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `angularDrag` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `drag` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forceAngle` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forceMagnitude` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forceTarget` | `EffectorSelection2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forceVariation` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useGlobalAngle` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colliderMask` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useColliderMask` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Shader
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `isSupported` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `keywordSpace` | `LocalKeywordSpace (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maximumLOD` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `passCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderQueue` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `subshaderCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `FindPassTagValue` | `ShaderTagId (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindPassTagValue` | `ShaderTagId (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindPropertyIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSubshaderTagValue` | `ShaderTagId (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindTextureStack` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetDependency` | `Shader` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPassCountInSubshader` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyAttributes` | `string[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyDefaultFloatValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyDefaultVectorValue` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyDescription` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyFlags` | `ShaderPropertyFlags (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyNameId` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyRangeLimits` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyTextureDefaultName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyTextureDimension` | `TextureDimension (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyType` | `ShaderPropertyType (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemColliderData
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetCollider` | `Component` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetColliderCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Vector3
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `magnitude` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `normalized` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sqrMagnitude` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `x` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `z` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Normalize` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Scale` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Set` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Rect
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `center` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `height` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `max` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `min` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `position` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `size` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `width` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `x` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `xMax` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `xMin` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `y` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `yMax` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `yMin` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Contains` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Contains` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Contains` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Overlaps` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Overlaps` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Set` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CompositeCollider2D
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `edgeRadius` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `offsetDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pathCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pointCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `vertexDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `attachedRigidbody` | `Rigidbody2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounciness` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `composite` | `CompositeCollider2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `density` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `errorState` | `ColliderErrorState2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `friction` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isTrigger` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `offset` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shapeCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `PhysicsMaterial2D` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `usedByComposite` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `usedByEffector` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GenerateGeometry` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPath` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPath` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPathPointCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Cast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClosestPoint` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Distance` | `ColliderDistance2D (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetContacts` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShapeHash` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShapes` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetShapes` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouching` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouching` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouching` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouchingLayers` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsTouchingLayers` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OverlapCollider` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OverlapCollider` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OverlapPoint` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Motion
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `apparentSpeed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `averageAngularSpeed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `averageDuration` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `averageSpeed` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isHumanMotion` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isLooping` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `legacy` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### MeshRenderer
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `additionalVertexStreams` | `Mesh (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enlightenVertexStream` | `Mesh (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `subMeshStartIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `allowOcclusionWhenDynamic` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `forceRenderingOff` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isPartOfStaticBatch` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isVisible` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightmapIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightmapScaleOffset` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightProbeProxyVolumeOverride` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lightProbeUsage` | `LightProbeUsage (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localBounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `localToWorldMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `materials` | `Material[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `motionVectorGenerationMode` | `MotionVectorGenerationMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `probeAnchor` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rayTracingMode` | `RayTracingMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `realtimeLightmapIndex` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `realtimeLightmapScaleOffset` | `Vector4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `receiveShadows` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `reflectionProbeUsage` | `ReflectionProbeUsage (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rendererPriority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderingLayerMask` | `uint` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shadowCastingMode` | `ShadowCastingMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterial` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sharedMaterials` | `Material[]` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingLayerID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingLayerName` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortingOrder` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `staticShadowCaster` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `worldToLocalMatrix` | `Matrix4x4` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetClosestReflectionProbes` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetMaterials` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetSharedMaterials` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasPropertyBlock` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetBounds` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetLocalBounds` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPropertyBlock` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ParticleSystemColorBySpeedModule
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `color` | `ParticleSystemMinMaxGradient` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `range` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AnimatorControllerParameter
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `defaultBool` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `defaultFloat` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `defaultInt` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `nameHash` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `type` | `AnimatorControllerParameterType (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Avatar
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AvatarID` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsHuman` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsLoaded` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Wearer` | `Player` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetHeight` | `float` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInitialHeight` | `float` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasBone` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasParameter` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetParameter` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetParameter` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetParameter` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Bounds
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `center` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `extents` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `max` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `min` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `size` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClosestPoint` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Contains` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Encapsulate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Encapsulate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Expand` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Expand` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IntersectRay` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IntersectRay` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Intersects` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetMinMax` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SqrDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ToString` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Component
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetComponent` | `object (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetComponentInChildren` | `object (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetComponentsInChildren` | `object[] (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetComponentInParent` | `object (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetComponentsInParent` | `object[] (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetComponents` | `object[] (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetComponents` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `TryGetComponent` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |

# UnityEngine_AILuaModule

## Constructors:
- NewNavMeshData()
- NewNavMeshData()

## Enums:

## Wrappers:
### NavMeshHit
#### Struct
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `distance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hit` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mask` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `normal` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `position` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### NavMeshAgent
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `acceleration` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `agentTypeID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `angularSpeed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `areaMask` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `autoBraking` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `autoRepath` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `autoTraverseOffMeshLink` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `avoidancePriority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `baseOffset` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `currentOffMeshLinkData` | `OffMeshLinkData (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `desiredVelocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `destination` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasPath` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `height` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isOnNavMesh` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isOnOffMeshLink` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isPathStale` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isStopped` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `navMeshOwner` | `UnityObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `nextOffMeshLinkData` | `OffMeshLinkData (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `nextPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `obstacleAvoidanceType` | `ObstacleAvoidanceType (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `path` | `NavMeshPath (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pathEndPosition` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pathPending` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pathStatus` | `NavMeshPathStatus (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `radius` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `remainingDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `speed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `steeringTarget` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `stoppingDistance` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `updatePosition` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `updateRotation` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `updateUpAxis` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `velocity` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `enabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isActiveAndEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `gameObject` | `GameObject` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `tag` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `transform` | `Transform` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ActivateCurrentOffMeshLink` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CalculatePath` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompleteOffMeshLink` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindClosestEdge` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetAreaCost` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Move` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Raycast` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ResetPath` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SamplePathPosition` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetAreaCost` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetDestination` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetPath` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Warp` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CompareTag` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### NavMeshData
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `position` | `Vector3` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rotation` | `Quaternion` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sourceBounds` | `Bounds` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `name` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Equals` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInstanceID` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |

# UnityEngine_UILuaModule

## Constructors:
- NewAnimationTriggers()
- NewFontData()

## Enums:

## Wrappers:
### HorizontalLayoutGroup
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CalculateLayoutInputHorizontal` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CalculateLayoutInputVertical` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLayoutHorizontal` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLayoutVertical` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### VerticalLayoutGroup
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CalculateLayoutInputHorizontal` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CalculateLayoutInputVertical` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLayoutHorizontal` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLayoutVertical` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Button
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `animationTriggers` | `AnimationTriggers` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animator` | `Animator` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colors` | `ColorBlock (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `image` | `Image` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `interactable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `navigation` | `Navigation (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spriteState` | `SpriteState (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetGraphic` | `Graphic (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `OnPointerClick` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnSubmit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectable` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnDown` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnLeft` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnRight` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnUp` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsInteractable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnDeselect` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnMove` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerDown` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerUp` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnSelect` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Select` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Mask
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `graphic` | `Graphic (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `rectTransform` | `RectTransform (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `showMaskGraphic` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetModifiedMaterial` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsRaycastLocationValid` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MaskEnabled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### ToggleGroup
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `allowSwitchOff` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ActiveToggles` | `IEnumerable<Toggle>` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AnyTogglesOn` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `EnsureValidState` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetFirstActiveToggle` | `Toggle` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `NotifyToggleOn` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RegisterToggle` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetAllTogglesOff` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UnregisterToggle` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### CanvasScaler
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `defaultSpriteDPI` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `dynamicPixelsPerUnit` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fallbackScreenDPI` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `matchWidthOrHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `referencePixelsPerUnit` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `referenceResolution` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `scaleFactor` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Toggle
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `graphic` | `Graphic (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `group` | `ToggleGroup` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isOn` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animationTriggers` | `AnimationTriggers` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animator` | `Animator` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colors` | `ColorBlock (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `image` | `Image` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `interactable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `navigation` | `Navigation (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spriteState` | `SpriteState (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetGraphic` | `Graphic (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GraphicUpdateComplete` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LayoutComplete` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerClick` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnSubmit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Rebuild` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetIsOnWithoutNotify` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectable` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnDown` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnLeft` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnRight` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnUp` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsInteractable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnDeselect` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnMove` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerDown` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerUp` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnSelect` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Select` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Image
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `alphaHitTestMinimumThreshold` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fillAmount` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fillCenter` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fillClockwise` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fillOrigin` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flexibleHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flexibleWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `hasBorder` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `layoutPriority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mainTexture` | `Texture` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `material` | `Material` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `overrideSprite` | `Sprite (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pixelsPerUnit` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pixelsPerUnitMultiplier` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preferredHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preferredWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preserveAspect` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sprite` | `Sprite (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useSpriteMesh` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CalculateLayoutInputHorizontal` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CalculateLayoutInputVertical` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DisableSpriteOptimizations` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsRaycastLocationValid` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnAfterDeserialize` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnBeforeSerialize` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetNativeSize` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AnimationTriggers
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `disabledTrigger` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `highlightedTrigger` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `normalTrigger` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pressedTrigger` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `selectedTrigger` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Slider
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `fillRect` | `RectTransform (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `handleRect` | `RectTransform (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `normalizedValue` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `value` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wholeNumbers` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animationTriggers` | `AnimationTriggers` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animator` | `Animator` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colors` | `ColorBlock (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `image` | `Image` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `interactable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `navigation` | `Navigation (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spriteState` | `SpriteState (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetGraphic` | `Graphic (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `FindSelectableOnDown` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnLeft` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnRight` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnUp` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GraphicUpdateComplete` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LayoutComplete` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnDrag` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnInitializePotentialDrag` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnMove` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerDown` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Rebuild` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetDirection` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetValueWithoutNotify` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectable` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsInteractable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnDeselect` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerUp` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnSelect` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Select` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### FontData
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `alignByGeometry` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `alignment` | `TextAnchor (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `bestFit` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `font` | `Font (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontSize` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontStyle` | `FontStyle (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `horizontalOverflow` | `HorizontalWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lineSpacing` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `maxSize` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minSize` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `richText` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `verticalOverflow` | `VerticalWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Scrollbar
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `handleRect` | `RectTransform (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `numberOfSteps` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `size` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `value` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animationTriggers` | `AnimationTriggers` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animator` | `Animator` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colors` | `ColorBlock (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `image` | `Image` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `interactable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `navigation` | `Navigation (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spriteState` | `SpriteState (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetGraphic` | `Graphic (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `FindSelectableOnDown` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnLeft` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnRight` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnUp` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GraphicUpdateComplete` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LayoutComplete` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnBeginDrag` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnDrag` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnInitializePotentialDrag` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnMove` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerDown` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerUp` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Rebuild` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetDirection` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetValueWithoutNotify` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectable` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsInteractable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnDeselect` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnSelect` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Select` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Dropdown
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `alphaFadeSpeed` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `captionImage` | `Image` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `captionText` | `Text` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `itemImage` | `Image` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `itemText` | `Text` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `template` | `RectTransform (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `value` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animationTriggers` | `AnimationTriggers` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animator` | `Animator` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colors` | `ColorBlock (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `image` | `Image` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `interactable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `navigation` | `Navigation (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spriteState` | `SpriteState (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetGraphic` | `Graphic (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AddOptions` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddOptions` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `AddOptions` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ClearOptions` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Hide` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnCancel` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerClick` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnSubmit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RefreshShownValue` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetValueWithoutNotify` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Show` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectable` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnDown` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnLeft` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnRight` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnUp` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsInteractable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnDeselect` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnMove` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerDown` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerUp` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnSelect` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Select` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Selectable
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `animationTriggers` | `AnimationTriggers` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animator` | `Animator` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colors` | `ColorBlock (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `image` | `Image` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `interactable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `navigation` | `Navigation (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spriteState` | `SpriteState (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetGraphic` | `Graphic (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `FindSelectable` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnDown` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnLeft` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnRight` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnUp` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsInteractable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnDeselect` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnMove` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerDown` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerUp` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnSelect` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Select` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### LayoutElement
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `flexibleHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flexibleWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ignoreLayout` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `layoutPriority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preferredHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preferredWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CalculateLayoutInputHorizontal` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CalculateLayoutInputVertical` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Shadow
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `effectColor` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `effectDistance` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `useGraphicAlpha` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ModifyMesh` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### GridLayoutGroup
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `cellSize` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `constraintCount` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spacing` | `Vector2` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CalculateLayoutInputHorizontal` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CalculateLayoutInputVertical` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLayoutHorizontal` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetLayoutVertical` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Outline
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ModifyMesh` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Text
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `alignByGeometry` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `alignment` | `TextAnchor (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cachedTextGenerator` | `TextGenerator (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `cachedTextGeneratorForLayout` | `TextGenerator (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flexibleHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flexibleWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `font` | `Font (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontSize` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `fontStyle` | `FontStyle (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `horizontalOverflow` | `HorizontalWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `layoutPriority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `lineSpacing` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `mainTexture` | `Texture` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `pixelsPerUnit` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preferredHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preferredWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `resizeTextForBestFit` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `resizeTextMaxSize` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `resizeTextMinSize` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `supportRichText` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `text` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `verticalOverflow` | `VerticalWrapMode (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CalculateLayoutInputHorizontal` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CalculateLayoutInputVertical` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FontTextureChanged` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetGenerationSettings` | `TextGenerationSettings (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### InputField
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `asteriskChar` | `char` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `caretBlinkRate` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `caretColor` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `caretPosition` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `caretWidth` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `characterLimit` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `customCaretColor` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flexibleHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `flexibleWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `isFocused` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `keyboardType` | `TouchScreenKeyboardType (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `layoutPriority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `minWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `multiLine` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `placeholder` | `Graphic (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preferredHeight` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `preferredWidth` | `float` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `readOnly` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `selectionAnchorPosition` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `selectionColor` | `Color` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `selectionFocusPosition` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shouldActivateOnSelect` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `shouldHideMobileInput` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `text` | `string` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `textComponent` | `Text` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `touchScreenKeyboard` | `TouchScreenKeyboard (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `wasCanceled` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animationTriggers` | `AnimationTriggers` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `animator` | `Animator` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `colors` | `ColorBlock (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `image` | `Image` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `interactable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `navigation` | `Navigation (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `spriteState` | `SpriteState (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `targetGraphic` | `Graphic (invalid)` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `ActivateInputField` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CalculateLayoutInputHorizontal` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `CalculateLayoutInputVertical` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DeactivateInputField` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ForceLabelUpdate` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GraphicUpdateComplete` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LayoutComplete` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MoveTextEnd` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MoveTextStart` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnBeginDrag` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnDeselect` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnDrag` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnEndDrag` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerClick` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerDown` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnSelect` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnSubmit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnUpdateSelected` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ProcessEvent` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Rebuild` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetTextWithoutNotify` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectable` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnDown` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnLeft` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnRight` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindSelectableOnUp` | `Selectable` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsInteractable` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnMove` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerEnter` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerExit` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `OnPointerUp` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Select` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### GraphicRaycaster
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `blockingMask` | `LayerMask` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `eventCamera` | `Camera` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `ignoreReversedGraphics` | `bool` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `renderOrderPriority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `sortOrderPriority` | `int` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Raycast` | `void` | `ANY` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |

# _CVRSpecialLuaModule

## Constructors:

## Enums:

## Wrappers:
### Avatar
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AvatarID` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsHuman` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsLoaded` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Wearer` | `Player` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `GetHeight` | `float` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetInitialHeight` | `float` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasBone` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `HasParameter` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetParameter` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetParameter` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `SetParameter` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### InstancesAPI
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `InstanceID` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `InstanceName` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `InstancePrivacy` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsConnected` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsHomeInstance` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Ping` | `int` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### AvatarAPI
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CurrentAvatar` | `Avatar` | `CLIENT` | `AVATAR` | `ANY` | `ANY` |
| `LocalAvatar` | `Avatar` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### Player
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `Avatar` | `Avatar` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Core` | `CoreParameters` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsLocal` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsRemote` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `UserID` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Username` | `string` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AddForce` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `GetForward` | `Vector3` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetGravity` | `Vector3` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetGravityDirection` | `Vector3` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetPosition` | `Vector3` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetRotation` | `Quaternion` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetViewPointPosition` | `Vector3` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetViewPointRotation` | `Quaternion` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetVoicePointPosition` | `Vector3` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GetVoicePointRotation` | `Quaternion` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LaunchCharacter` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `PauseGroundConstraint` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `ResetAllForces` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `Respawn` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `SetBodyControlHeadWeight` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `SetBodyControlLeftArmWeight` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `SetBodyControlLeftLegWeight` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `SetBodyControlLocomotionWeight` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `SetBodyControlPelvisWeight` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `SetBodyControlRightArmWeight` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `SetBodyControlRightLegWeight` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `SetControllerVelocity` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `SetFlight` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `SetImmobilized` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `SetPosition` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `SetRotation` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `TeleportPlayerTo` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `TeleportPlayerTo` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `TeleportPlayerTo` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
| `TeleportPlayerTo` | `void` | `CLIENT` | `ALL_BUT_EVENTS` | `LOCAL` | `ANY` |
### CoreParameters
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `CancelEmote` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Crouching` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `DistanceTo` | `float` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Emote` | `int` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Flying` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GestureLeft` | `float` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GestureLeftIdx` | `float` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GestureRight` | `float` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `GestureRightIdx` | `float` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Grounded` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MovementX` | `float` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `MovementY` | `float` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Prone` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Sitting` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Swimming` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `Toggle` | `int` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `VisemeIdx` | `int` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `VisemeLoudness` | `float` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
### PlayerAPI
#### Instance Properties
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `AllPlayers` | `ReadOnlyCollection<Player>` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `LocalPlayer` | `Player` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `PlayerCount` | `int` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `RemotePlayers` | `ReadOnlyCollection<Player>` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
#### Instance Functions
| Name | Return Type | Environment | Object | Owner | Scope |
|------|-------------|-------------|--------|-------|-------|
| `FindPlayerByUserId` | `Player` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `FindPlayerByUsername` | `Player` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |
| `IsFriendsWith` | `bool` | `CLIENT` | `ALL_BUT_EVENTS` | `ANY` | `ANY` |

