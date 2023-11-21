<script>
  import { T, useFrame } from '@threlte/core'
  import { interactivity, Grid, MeshLineGeometry, MeshLineMaterial, OrbitControls } from '@threlte/extras'
  import { spring } from 'svelte/motion'
  import { LineCurve3, Vector3 } from 'three'

  interactivity()
  const scale = spring(1)
  let rotation = 0
  useFrame((state, delta) => {
    rotation += delta
  })



   // create a smooth curve from 4 points
   const curve = new LineCurve3(new Vector3(4, 4, 0), new Vector3(8, 8, 0))
  // convert curve to an array of 100 points
  const points = curve.getPoints(100)
</script>


<Grid
	infiniteGrid
	sectionColor="#4a4b4a"
	sectionSize={20}
	cellSize={20}
	fadeDistance={400}
/>

<T.PerspectiveCamera makeDefault position={[10, 100, 100]} fov={60}>
	<OrbitControls enableDamping />
</T.PerspectiveCamera>

<T.DirectionalLight position={[0, 10, 10]} castShadow />

<T.Mesh
  
  position.y={1}
  scale={$scale}
  on:pointerenter={() => scale.set(1.5)}
  on:pointerleave={() => scale.set(1)}
  castShadow
>
  <T.BoxGeometry args={[1, 2, 1]} />
  <T.MeshStandardMaterial color="hotpink" />
</T.Mesh>

<T.Mesh rotation.x={-Math.PI/2} receiveShadow>
  <T.CircleGeometry args={[4, 40]}/>
  <T.MeshStandardMaterial color="white" />
</T.Mesh>

<T.Mesh position.x={4} position.y={4}>
  <T.SphereGeometry />
  <T.MeshStandardMaterial color="white" />
</T.Mesh>

<T.Mesh position.x={8} position.y={8}>
  <T.SphereGeometry />
  <T.MeshStandardMaterial color="white" />
</T.Mesh>

<T.Mesh
  position.x={0}
  position.y={0}
  scale={1}
>
  <MeshLineGeometry
    {points}
    shape="taper"
  />
  <MeshLineMaterial color="#fe3d00" />
</T.Mesh>