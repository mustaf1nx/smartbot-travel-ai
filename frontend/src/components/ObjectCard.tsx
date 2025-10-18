import { Card, Badge, Group, Text } from "@mantine/core";
import { TravelObject } from "../types";

const stageColor: Record<string,string> = { hot:"red", warm:"yellow", cold:"blue" };

export default function ObjectCard({ o }: { o: TravelObject }) {
  return (
    <Card withBorder radius="lg">
      <Group justify="space-between">
        <Text fw={700}>{o.name}</Text>
        <Badge color={stageColor[o.lead_stage]}>{o.lead_stage.toUpperCase()}</Badge>
      </Group>
      <Text size="sm" mt="xs" c="dimmed">{o.address}</Text>
      <Text size="sm" mt="sm">{o.description_ai || "Описание обновляется..."}</Text>
      <Group mt="sm" gap="xs">
        <Badge variant="light">Рейтинг: {o.rating}</Badge>
        {o.category && <Badge variant="light">{o.category}</Badge>}
      </Group>
    </Card>
  );
}
