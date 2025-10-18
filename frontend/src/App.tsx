import { Container, Title, Group, Button } from "@mantine/core";
import { useEffect, useState } from "react";
import { fetchObjects, scanRegion, exportCSV, exportJSON } from "./api/client";
import MapView from "./components/MapView";
import Filters from "./components/Filters";
import TopLeads from "./components/TopLeads";
import { TravelObject } from "./types";

export default function App() {
  const [items, setItems] = useState<TravelObject[]>([]);

  const reload = async (params?: {category?:string; stage?:string}) => {
    const data = await fetchObjects(params);
    setItems(data);
  };

  useEffect(() => { reload(); }, []);

  return (
    <Container size="xl" py="lg">
      <Group justify="space-between">
        <Title order={2}>AI Travel Scout — Казахстан</Title>
        <Group>
          <Button component="a" href={exportCSV()} variant="light">Экспорт CSV</Button>
          <Button component="a" href={exportJSON()} variant="light">Экспорт JSON</Button>
        </Group>
      </Group>

      <Filters
        onScan={async (region)=>{ await scanRegion(region); await reload(); }}
        onFilter={(f)=>reload(f)}
      />

      <MapView items={items} />
      <Title order={3} mt="lg" mb="sm">Top-10 горячих лидов</Title>
      <TopLeads items={items} />
    </Container>
  );
}
