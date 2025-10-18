export type LeadStage = "hot" | "warm" | "cold";

export interface TravelObject {
  id: string;
  name: string;
  lat: number;
  lon: number;
  address?: string;
  category: string;
  phone?: string;
  email?: string;
  socials: string[];
  website?: string;
  description_ai?: string;
  rooms?: number;
  price_min?: number;
  price_max?: number;
  infra?: string[];
  rating: number;
  lead_stage: LeadStage;
}
