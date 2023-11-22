import { sveltekit } from '@sveltejs/kit/vite';



const config: UserConfig = {
plugins: [sveltekit()],
resolve: {
	alias: {
	three: 'three'
	},
	extensions: ['.mjs', '.js', '.ts', '.jsx', '.tsx', '.json']
},
optimizeDeps: {
	include: ['three']
},
ssr: {
	noExternal: ['three']
	}
};

export default config;