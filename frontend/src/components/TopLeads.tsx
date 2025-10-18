import { SimpleGrid } from "@mantine/core";
import { TravelObject } from "../types";
import ObjectCard from "./ObjectCard";

export default function TopLeads({ items }: { items: TravelObject[] }) {
  const top = [...items].sort((a,b)=>b.rating-a.rating).slice(0,10);
  return (
    <SimpleGrid cols={{ base: 1, sm: 2, md: 3 }}>
      {top.map(o => <ObjectCard key={o.id} o={o} />)}
    </SimpleGrid>
  );
}
