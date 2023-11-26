import type { Vector3 } from 'three';
type Link = {
	source: Vector3;
    destination: Vector3;
    color : string;
}
type Flow = {
	name: string;
    controlPoint: Vector3[];
    color : string;
    }

type Lan = {
    type: string;
    position: Vector3;
    color : string;
    }

type User = {
    position: Vector3;
    }

export type Links = Array<Link | null>
export type Flows = Array<Flow | null>
export type Lans = Array<Lan | null>
export type Users = Array<User | null>

type Day = {
	count: number
	day: number
	level: number
	month: string
	name: string
	year: number
}

export type Contributions = Array<Day | null>
