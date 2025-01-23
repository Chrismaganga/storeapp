import * as React from 'react'
import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/search')({
  component: SearchComponent,
})

function SearchComponent() {
  return (
    <div className="p-2">
      <h3>Search</h3>
    </div>
  )
}
