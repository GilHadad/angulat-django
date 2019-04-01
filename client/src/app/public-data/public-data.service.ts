import {Inject, Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {APP_CONFIG, AppConfig} from '../app.conf';

const endpoint = '/api/get-products/'


@Injectable()
export class PublicDataService {
  private url: string;
  constructor(private http: HttpClient, @Inject(APP_CONFIG) private appConfig: AppConfig) {
    this.url = appConfig.baseUrl + endpoint;
  }

  getProducts () {
    return this.http.get<any[]>(this.url).toPromise().then(res => {
        console.log(res);
    })
  }

  test() {
    return this.http.get<any[]>('http://localhost:4200/api/api/get-products/').toPromise().then(res => {
        console.log(res);
    })
  }

  


}