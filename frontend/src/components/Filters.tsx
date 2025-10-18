import { Button, Group, Select, TextInput } from "@mantine/core";
import { useState } from "react";

export default function Filters({
  onScan, onFilter
}: { onScan: (region: string)=>void; onFilter: (f:{category?:string; stage?:string})=>void }) {
  const [region, setRegion] = useState("Алматы");
  const [category, setCategory] = useState<string | null>(null);
  const [stage, setStage] = useState<string | null>(null);

  return (
    <Group wrap="wrap">
      <TextInput label="Регион" value={region} onChange={(e)=>setRegion(e.currentTarget.value)} />
      <Select label="Категория" data={[
        {value:"lux_glamping", label:"Люкс глэмпинг"},
        {value:"family_guesthouse", label:"Семейный гостевой дом"},
        {value:"eco", label:"Эко"},
        {value:"ethno_yurt", label:"Этно (юрты)"},
        {value:"mountain_cabin", label:"Горные домики"},
        {value:"other", label:"Другое"},
      ]} value={category} onChange={setCategory} clearable />
      <Select label="Статус лида" data={[
        {value:"hot", label:"Горячий"},
        {value:"warm", label:"Тёплый"},
        {value:"cold", label:"Холодный"},
      ]} value={stage} onChange={setStage} clearable />
      <Button onClick={()=>onScan(region)}>Сканировать 2GIS</Button>
      <Button variant="light" onClick={()=>onFilter({category:category||undefined, stage:stage||undefined})}>
        Применить фильтры
      </Button>
    </Group>
  );
}
