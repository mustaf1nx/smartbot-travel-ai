import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
});

export const fetchObjects = async (params?: { category?: string; stage?: string }) => {
  const q = new URLSearchParams();
  if (params?.category) q.set("category", params.category);
  if (params?.stage) q.set("stage_filter", params.stage);
  const { data } = await api.get(`/objects?${q.toString()}`);
  return data;
};

export const scanRegion = async (region: string) => {
  const { data } = await api.post(`/objects/scan?region=${encodeURIComponent(region)}`);
  return data;
};

export const exportCSV = () => `${api.defaults.baseURL}/exports/csv`;
export const exportJSON = () => `${api.defaults.baseURL}/exports/json`;

export default api;
