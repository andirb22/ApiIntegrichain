import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { BookComponent } from './book/book.component';
import { AddBookComponent } from './book/add-book.component';
import { UpdateBookComponent } from './book/update-book.component';

const routes: Routes = [
  { path: 'books', component: BookComponent },
  { path: 'add', component: AddBookComponent },
  { path: 'update/:id', component: UpdateBookComponent },
  { path: '', redirectTo: '/books', pathMatch: 'full'}
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ],
  declarations: []
})
export class AppRoutingModule { }