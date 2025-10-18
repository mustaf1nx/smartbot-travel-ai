import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { TravelObject } from "../types";

export default function MapView({ items }: { items: TravelObject[] }) {
  const center: [number, number] = [43.238, 76.945]; // Алматы
  return (
    <div style={{ height: 500, borderRadius: 12, overflow: "hidden" }}>
      <MapContainer center={center} zoom={6} style={{ height: "100%", width: "100%" }}>
        <TileLayer
          attribution='&copy; OpenStreetMap'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {items.map(o => (
          <Marker key={o.id} position={[o.lat, o.lon]}>
            <Popup>
              <b>{o.name}</b><br/>{o.address || "—"}<br/>Рейтинг: {o.rating} ({o.lead_stage})
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
}
