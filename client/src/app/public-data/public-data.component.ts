import { Component, OnInit } from '@angular/core';
import { PublicDataService } from './public-data.service';

@Component({
  selector: 'app-public-data',
  templateUrl: './public-data.component.html',
  styleUrls: ['./public-data.component.scss'],
})
export class PublicDataComponent implements OnInit {

  constructor(private publicDataService: PublicDataService) { }

  ngOnInit() {
    this.publicDataService.getProducts();
    this.publicDataService.test();
  }

}
