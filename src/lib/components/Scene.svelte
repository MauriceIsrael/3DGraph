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
  const curve1 = new LineCurve3(new Vector3(4, 0, 4), new Vector3(8, 0, 8))
  // convert curve to an array of 100 points
  const points = curve1.getPoints(100)

  // create a smooth curve from 4 points
  const curve2 = new LineCurve3(new Vector3(-8, 20, 3), new Vector3(12, 20, 10))
  // convert curve to an array of 100 points
  let points2 = curve2.getPoints(100)
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

<!-- Disque vert clair-->
<T.Mesh position.y={40} rotation.x={-Math.PI/2} receiveShadow>
  <T.CircleGeometry args={[40, 100]}/>
  <T.MeshStandardMaterial color="green" transparent={true} opacity={0.5}/>
</T.Mesh>

<!-- Disque bleu cyan-->
<T.Mesh position.y={-20} rotation.x={-Math.PI/2} receiveShadow>
  <T.CircleGeometry args={[40, 100]}/>
  <T.MeshStandardMaterial color="cyan" transparent={true} opacity={0.5}/>
</T.Mesh>

<!-- Disque bleu clair-->
<T.Mesh position.y={0} rotation.x={-Math.PI/2} receiveShadow>
  <T.CircleGeometry args={[40, 100]}/>
  <T.MeshStandardMaterial color="lightblue" transparent={true} opacity={0.5}/>
</T.Mesh>

<!-- Disque bleu foncé-->
<T.Mesh position.y={20} rotation.x={-Math.PI/2} receiveShadow>
  <T.CircleGeometry args={[40, 100]}/>
  <T.MeshStandardMaterial color="darkblue" transparent={true} opacity={0.5}/>
</T.Mesh>

<!-- Spheres bleues-->
<T.Mesh position.x={4} position.z={4}>
  <T.SphereGeometry args={[1, 100]}/>
  <T.MeshStandardMaterial color="blue" />
</T.Mesh>

<T.Mesh position.x={8} position.z={8}>
  <T.SphereGeometry />
  <T.MeshStandardMaterial color="blue" />
</T.Mesh>

<T.Mesh position.x={0} position.y={0} scale={1}>
  <MeshLineGeometry {points} shape="none"/>
  <MeshLineMaterial color="#fe3d00" />
</T.Mesh>

<!-- Spheres jaunes-->
<T.Mesh position.x={-8} position.y={20} position.z={3}>
  <T.SphereGeometry args={[1, 100]}/>
  <T.MeshStandardMaterial color="yellow" />
</T.Mesh>

<T.Mesh position.x={12} position.y={20} position.z={10}>
  <T.SphereGeometry />
  <T.MeshStandardMaterial color="yellow" />
</T.Mesh>

<T.Mesh position.x={0} position.y={0} scale={1}>
  <MeshLineGeometry points={points2} shape="taper"/>
  <MeshLineMaterial color="yellow" />
</T.Mesh>