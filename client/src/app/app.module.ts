import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PublicDataComponent } from './public-data/public-data.component';
import { APP_CONFIG, appConfig } from './app.conf';
import { PublicDataService } from './public-data/public-data.service';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    PublicDataComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,

    HttpClientModule,
  ],
  providers: [
    PublicDataService,
    { provide: APP_CONFIG, useValue: appConfig },
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
