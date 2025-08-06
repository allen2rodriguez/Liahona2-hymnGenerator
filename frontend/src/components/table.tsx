import { useState } from "react";
import Table from "@cloudscape-design/components/table";
import Header from "@cloudscape-design/components/header";
import Pagination from "@cloudscape-design/components/pagination";
import TextFilter from "@cloudscape-design/components/text-filter";
import '@cloudscape-design/global-styles/index.css';
import hymnsData from '../../data.json';

type HymnItem = {
  date: string;
  closing: { link: string | null; number: number | null };
  opening: { link: string | null; number: number | null };
  sacrament: { link: string | null; number: number | null };
  intermediate: { link: string | null; number: number | null };
};

const items: HymnItem[] = hymnsData;

const columnDefinitions = [
  {
    id: 'date',
    header: 'Date',
    cell: (item: HymnItem) => item.date,
    sortingField: 'date',
    isRowHeader: true,
  },
  {
    id: 'opening',
    header: 'Opening Hymn',
    cell: (item: HymnItem) => (
      <a 
      href={item.opening.link ?? undefined} 
      target="_blank" rel="noopener noreferrer"
      style={{ color: '#42b4ff', textDecoration: 'underline' }}>
        {item.opening.number ?? 'None'}
      </a>
    ),
  },
  {
    id: 'sacrament',
    header: 'Sacrament Hymn',
    cell: (item: HymnItem) => (
      <a href={item.sacrament.link ?? undefined} target="_blank" rel="noopener noreferrer"
      style={{ color: '#42b4ff', textDecoration: 'underline' }}>
        {item.sacrament.number ?? 'None'}
      </a>
    ),
  },
  {
    id: 'intermediate',
    header: 'Intermediate Hymn',
    cell: (item: HymnItem) =>
      !item.intermediate.link ? (
        'None'
      ) : (
        <a href={item.intermediate.link} target="_blank" rel="noopener noreferrer"
        style={{ color: '#42b4ff', textDecoration: 'underline' }}>
          {item.intermediate.number}
        </a>
      ),
  },
  {
    id: 'closing',
    header: 'Closing Hymn',
    cell: (item: HymnItem) =>
      !item.closing.link ? (
        'None'
      ) : (
        <a href={item.closing.link} target="_blank" rel="noopener noreferrer"
        style={{ color: '#42b4ff', textDecoration: 'underline' }}>
          {item.closing.number}
        </a>
      )
  },
];

export default function HistoryTable() {
  const [selectedItems, setSelectedItems] = useState<HymnItem[]>([]);
  const [filteringText, setFilteringText] = useState("");
  const [currentPageIndex, setCurrentPageIndex] = useState(1);
  const [sortingColumn, setSortingColumn] = useState<any>(columnDefinitions[0]); // default to 'date'
  const [isDescending, setIsDescending] = useState(true);

  const pageSize = 5;

  // Filtering: check date and hymn numbers as strings
  const filteredItems = items.filter((item) => {
    const text = filteringText.toLowerCase();
    return (
      item.date.toLowerCase().includes(text) ||
      item.opening.number?.toString().includes(text) ||
      item.sacrament.number?.toString().includes(text) ||
      item.closing.number?.toString().includes(text) ||
      item.intermediate.number?.toString().includes(text)
    );
  });

  // Sorting
 const sortedItems = [...filteredItems].sort((a, b) => {
  const field = sortingColumn?.sortingField as keyof HymnItem;
  if (!field) return 0;

  const valA = a[field];
  const valB = b[field];

  if (valA === null || valA === undefined) return 1;
  if (valB === null || valB === undefined) return -1;

  if (valA < valB) return isDescending ? 1 : -1;
  if (valA > valB) return isDescending ? -1 : 1;
  return 0;
});


  const totalPages = Math.ceil(sortedItems.length / pageSize);

  // Pagination
  const paginatedItems = sortedItems.slice(
    (currentPageIndex - 1) * pageSize,
    currentPageIndex * pageSize
  );

  return (
    <div className="table-wrapper">
      <Table
        header={
          <Header
            counter={
              selectedItems.length
                ? `(${selectedItems.length}/${items.length})`
                : `(${items.length})`
            }
          >
            Hymn History
          </Header>
        }
        columnDefinitions={columnDefinitions}
        items={paginatedItems}
        selectionType="multi"
        selectedItems={selectedItems}
        onSelectionChange={({ detail }) => setSelectedItems(detail.selectedItems)}
        sortingColumn={sortingColumn}
        sortingDescending={isDescending}
        onSortingChange={({ detail }) => {
          setSortingColumn(detail.sortingColumn);
          setIsDescending(detail.isDescending ?? false);
        }}
        enableKeyboardNavigation
        trackBy="date"
        variant="container"
        filter={
          <TextFilter
            filteringPlaceholder="Find hymns"
            filteringText={filteringText}
            filteringAriaLabel="Filter hymns"
            onChange={({ detail }) => setFilteringText(detail.filteringText)}
          />
        }
        pagination={
          <Pagination
            currentPageIndex={currentPageIndex}
            pagesCount={totalPages}
            onChange={({ detail }) => setCurrentPageIndex(detail.currentPageIndex)}
          />
        }
      />
    </div>
  );
}
